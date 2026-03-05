import streamlit as st
import boto3
import json

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

bedrock = boto3.client("bedrock-runtime", region_name=REGION)

st.set_page_config(page_title="AWS Community Day Chennai 2026 - ChatBot", page_icon="🤖")
st.title("AWS Community Day Chennai 2026 - ChatBot")

user_input = st.text_area("Enter your message")

if st.button("Send") and user_input:

    with st.spinner("Thinking..."):

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "temperature": 0.7,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user_input
                            }
                        ]
                    }
                ]
            })
        )

        response_body = json.loads(response["body"].read())
        answer = response_body["content"][0]["text"]

    st.subheader("Response")
    st.write(answer)