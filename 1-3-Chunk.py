text = """
Amazon Bedrock is a fully managed service that makes foundation models 
available via an API. It helps developers build and scale generative AI applications.
Chunking is important because large documents cannot be directly embedded at once.
Overlap helps preserve context between chunks.
"""

def chunk_without_overlap(text, chunk_size=80):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def chunk_with_overlap(text, chunk_size=80, overlap=20):
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(text), step):
        chunks.append(text[i:i+chunk_size])
    return chunks

chunks_no_overlap = chunk_without_overlap(text)
chunks_with_overlap = chunk_with_overlap(text)
print("Original Text")
print("="*50)
print(text)
print("\n" + "="*50)
print("❌ WITHOUT OVERLAP")
print("="*50)

for i, chunk in enumerate(chunks_no_overlap, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)


print("\n\n" + "="*50)
print("✅ WITH OVERLAP")
print("="*50)

for i, chunk in enumerate(chunks_with_overlap, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)