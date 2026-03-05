import boto3
import json
import numpy as np

bedrock = boto3.client(service_name='bedrock-runtime')

def get_embedding(text):
    response = bedrock.invoke_model(
        modelId='amazon.titan-embed-text-v1',
        body=json.dumps({"inputText": text}),
        contentType='application/json'
    )
    response_body = response['body'].read().decode('utf-8')
    return np.array(json.loads(response_body)['embedding'])

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

variable1 = [
    "Production server is down",
    "High CPU utilization",
    "Memory leak detected",
    "Everything is working fine",
    "Deployed on Friday evening",
    "Pizza party in office",
    "Cloud cost exceeded budget"
]

variable2 = input("\nEnter your phrase for comparison: ").strip()

if not variable2:
    print("⚠️ You must enter a phrase!")
    exit()

print("\nGenerating embedding for your input...\n")

query_embedding = get_embedding(variable2)

results = []

for word in variable1:
    emb = get_embedding(word)
    similarity = cosine_similarity(query_embedding, emb)
    
    results.append({
        "word": word,
        "similarity": similarity
    })

results = sorted(results, key=lambda x: x["similarity"], reverse=True)

print("\nRanking based on similarity:\n")

for rank, item in enumerate(results, 1):
    print(f"{rank}. {item['word']} → {item['similarity']:.4f}")