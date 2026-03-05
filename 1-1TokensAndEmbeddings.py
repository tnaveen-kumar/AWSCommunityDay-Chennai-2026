import boto3
import json
import time

bedrock = boto3.client("bedrock-runtime")
input_text = "Amazon S3 is amazing"
response = bedrock.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({
        "inputText": input_text
    }),
    contentType="application/json"
)
response_body = json.loads(response['body'].read())
embedding = response_body["embedding"]
token_count = response_body["inputTextTokenCount"]
print("------ AWS Bedrock Embedding Details ------")
print("Token count:", token_count)
print("Embedding dimension:", len(embedding))

print("\nFirst 5 embedding values:")
print(embedding[:5])

print("\nLast 5 embedding values:")
print(embedding[-5:])
print("\nEmbedding value type:", type(embedding[0]))
print("\n------ AWS Response Metadata ------")
print(json.dumps(response["ResponseMetadata"], indent=2))