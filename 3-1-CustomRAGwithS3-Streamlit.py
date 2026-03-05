import streamlit as st
import boto3
import uuid
import json
import io
from pypdf import PdfReader
from botocore.exceptions import ClientError
from typing import List

REGION = "us-east-1"
DOC_BUCKET = "acd-2026-raw"
VECTOR_BUCKET = "acd-2026-raw-vector"
INDEX_NAME = "demo-index"
EMBED_MODEL = "amazon.titan-embed-text-v2:0"
LLM_MODEL = "anthropic.claude-3-haiku-20240307-v1:0"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 150
TOP_K = 20

s3 = boto3.client("s3", region_name=REGION)
bedrock = boto3.client("bedrock-runtime", region_name=REGION)
s3vectors = boto3.client("s3vectors", region_name=REGION)


def chunk_text(text: str) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def extract_text_from_pdf(file_bytes):
    reader = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def extract_text_from_txt(file_bytes):
    return file_bytes.decode("utf-8")


def create_embedding(text):
    response = bedrock.invoke_model(
        modelId=EMBED_MODEL,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"inputText": text})
    )

    body = json.loads(response["body"].read())
    return body["embedding"]


def generate_answer(context, question):

    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    response = bedrock.invoke_model(
        modelId=LLM_MODEL,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "temperature": 0.5,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        })
    )

    response_body = json.loads(response["body"].read())

    return response_body["content"][0]["text"]


def store_chunk(chunk, source_file):

    embedding = create_embedding(chunk)

    s3vectors.put_vectors(
        vectorBucketName=VECTOR_BUCKET,
        indexName=INDEX_NAME,
        vectors=[{
            "key": str(uuid.uuid4()),
            "data": {"float32": embedding},
            "metadata": {
                "text": chunk,
                "source": source_file
            }
        }]
    )


def search_vectors(query):

    query_embedding = create_embedding(query)

    response = s3vectors.query_vectors(
        vectorBucketName=VECTOR_BUCKET,
        indexName=INDEX_NAME,
        queryVector={
            "float32": query_embedding
        },
        topK=TOP_K,
        returnMetadata=True
    )

    return response.get("vectors", [])


st.title("AWS Community Day Chennai 2026 - S3 Vectors Demo")

uploaded_file = st.file_uploader("Upload Document", type=["pdf", "txt"])

if uploaded_file:

    s3.upload_fileobj(uploaded_file, DOC_BUCKET, uploaded_file.name)

    st.success(f"Uploaded {uploaded_file.name}")


if st.button("Embed Documents"):

    files = s3.list_objects_v2(Bucket=DOC_BUCKET)

    if "Contents" in files:

        for file in files["Contents"]:

            obj = s3.get_object(Bucket=DOC_BUCKET, Key=file["Key"])

            file_bytes = obj["Body"].read()

            if file["Key"].lower().endswith(".pdf"):
                text = extract_text_from_pdf(file_bytes)

            elif file["Key"].lower().endswith(".txt"):
                text = extract_text_from_txt(file_bytes)

            else:
                continue

            chunks = chunk_text(text)

            for chunk in chunks:
                store_chunk(chunk, file["Key"])

            st.success(f"Embedded {file['Key']}")


st.header("Chat")

query = st.text_input("Ask question")

if st.button("Search") and query:

    results = search_vectors(query)

    if not results:
        st.warning("No relevant context found.")

    else:

        context = "\n\n".join(
            [r["metadata"]["text"] for r in results]
        )

        answer = generate_answer(context, query)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Retrieved Context"):
            st.write(context)