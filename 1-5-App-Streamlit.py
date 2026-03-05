import streamlit as st
import boto3
import json

REGION = "us-east-1"
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

bedrock = boto3.client("bedrock-runtime", region_name=REGION)

st.set_page_config(page_title="AWS Community Day Chennai 2026 - ChatBot(V2)", page_icon="🤖")
st.title("AWS Community Day Chennai 2026 - ChatBot(V2)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:

    # Add user message to memory
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    bedrock_messages = []

    for msg in st.session_state.messages:
        bedrock_messages.append({
            "role": msg["role"],
            "content": [
                {
                    "type": "text",
                    "text": msg["content"]
                }
            ]
        })

    with st.spinner("Thinking..."):

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "temperature": 0.7,
                "messages": bedrock_messages
            })
        )

        response_body = json.loads(response["body"].read())
        assistant_reply = response_body["content"][0]["text"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)