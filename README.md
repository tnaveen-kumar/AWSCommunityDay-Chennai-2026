# AWS Community Day Chennai 2026 - Beyond Object Storage: Getting Started with Amazon S3 Vectors

This repository contains demo applications and scripts for learning AWS Bedrock, embeddings, vector search, and RAG (Retrieval Augmented Generation) using Amazon S3 Vector capabilities.

## Overview

The project demonstrates progressive learning from basic chatbots to advanced RAG systems using AWS services:
- Amazon Bedrock (Claude 3 Haiku, Titan Embeddings)
- Amazon S3 Vector Search
- Streamlit for UI
- Python

## Prerequisites

- AWS CLI v2 installed and configured
- Python 3.x with pip
- AWS account with Bedrock access enabled
- Required Python packages:
  ```
  pip install streamlit boto3 pypdf colorama s3vectors-embed-cli
  ```

## Project Structure

Follow the scripts in this order for the best learning experience:

### 1. Understanding Embeddings & Vector Fundamentals

#### `1-1TokensAndEmbeddings.py` - Understanding Embeddings
Demonstrates how text is converted to vector embeddings using Amazon Titan.

**Key Concepts:**
- Token counting
- Embedding dimensions (1024-dimensional vectors)
- Vector representation of text
- AWS Bedrock embedding API

**Run:**
```bash
python 1-1TokensAndEmbeddings.py
```

**Output:**
- Token count for input text
- Embedding dimension size
- Sample embedding values
- Response metadata

#### `1-2-Ranking.py` - Semantic Similarity Search
Interactive script demonstrating cosine similarity for semantic search.

**Features:**
- User input comparison against predefined phrases
- Cosine similarity calculation
- Ranked results by semantic relevance
- Real-time embedding generation

**Run:**
```bash
python 1-2-Ranking.py
```

**Example Use Case:**
Compare "server crashed" against phrases like "Production server is down" to find semantic matches.

#### `1-3-Chunk.py` - Text Chunking Strategies
Demonstrates text chunking with and without overlap for document processing.

**Key Concepts:**
- Fixed-size chunking
- Overlapping chunks for context preservation
- Chunk size: 80 characters
- Overlap: 20 characters

**Run:**
```bash
python 1-3-Chunk.py
```

### 2. Basic Chatbot Applications

#### `1-4-App-Streamlit.py` - Simple Chatbot
Basic Streamlit chatbot using Claude 3 Haiku. Single-turn conversation with no memory.

**Features:**
- Text input interface
- Direct Bedrock API integration
- Single request/response flow

**Run:**
```bash
streamlit run 1-4-App-Streamlit.py
```

#### `1-5-App-Streamlit.py` - Conversational Chatbot
Enhanced version with conversation memory using Streamlit session state.

**Features:**
- Chat interface with message history
- Multi-turn conversations
- Session state management
- Persistent conversation context

**Run:**
```bash
streamlit run 1-5-App-Streamlit.py
```

### 3. AWS S3 Vector Search

#### `2-2-AWS-S3VectorBucket-Manual.ps1` - Manual S3 Vector Setup
PowerShell script with step-by-step commands for creating and querying S3 vector buckets.

**Operations:**
1. Create S3 vector bucket
2. Create vector index (1024 dimensions, cosine metric)
3. Insert sample vectors
4. Query vectors
5. List indexes
6. Retrieve vector metadata

**Run:**
```powershell
# Follow commands in the script manually
```

### 4. Advanced RAG Application

#### `3-1-CustomRAGwithS3-Streamlit.py` - Full RAG System
Complete Retrieval Augmented Generation system with PDF and TXT processing and vector search.

**Architecture:**
1. Document upload to S3 (`acd-2026-raw`)
2. Text extraction and chunking
3. Embedding generation (Titan)
4. Vector storage (S3 Vectors)
5. Semantic search on user queries
6. Context-aware answer generation (Claude)

**Features:**
- PDF and TXT document upload
- Automatic text extraction
- Intelligent chunking (500 chars, 150 overlap)
- Vector embedding and indexing
- Top-K retrieval (K=20)
- LLM-powered answer generation
- Context display

**Configuration:**
- Document bucket: `acd-2026-raw`
- Vector bucket: `acd-2026-raw-vector`
- Index: `demo-index`
- Chunk size: 500 characters
- Chunk overlap: 150 characters
- Top K results: 20
- Max tokens: 1000
- Temperature: 0.5

**Run:**
```bash
streamlit run 3-1-CustomRAGwithS3-Streamlit.py
```

**Workflow:**
1. Upload PDF documents
2. Click "Embed Documents" to process and index
3. Ask questions in the chat interface
4. View AI-generated answers with source context

## AWS Services Used

### Amazon Bedrock
- **Claude 3 Haiku**: Fast, cost-effective LLM for chat and generation
- **Titan Embeddings v2**: 1024-dimensional text embeddings

### Amazon S3 Vectors
- Vector storage and indexing
- Cosine similarity search
- Metadata storage
- Scalable vector database

### Amazon S3
- Document storage
- Raw file management

## Key Concepts Demonstrated

### Embeddings
Converting text into numerical vectors that capture semantic meaning. Similar concepts have similar vectors.

### Vector Search
Finding semantically similar content using mathematical distance metrics (cosine similarity).

### Chunking
Breaking large documents into smaller pieces for embedding and retrieval.

### RAG (Retrieval Augmented Generation)
Combining vector search with LLMs to provide accurate, context-aware answers from your own documents.

### Semantic Similarity
Measuring how similar two pieces of text are in meaning, not just keywords.

## Learning Path

Follow these scripts in order for the best learning experience:

1. **`1-1TokensAndEmbeddings.py`** - Understand how text becomes vectors
2. **`1-2-Ranking.py`** - Learn semantic similarity and ranking
3. **`1-3-Chunk.py`** - See how documents are chunked for processing
4. **`1-4-App-Streamlit.py`** - Build a simple chatbot
5. **`1-5-App-Streamlit.py`** - Add conversation memory to your chatbot
7. **`2-2-AWS-S3VectorBucket-Manual.ps1`** - Learn S3 vector operations manually
8. **`3-1-CustomRAGwithS3-Streamlit.py`** - Build a complete RAG system

### Supporting Scripts
- **`10---Data-load-s3vector-app-demo.ps1`** - Load demo data for 2-1 (run before step 6)

## Configuration

All scripts use `us-east-1` region by default. Update the `REGION` variable if needed.

### Required AWS Permissions
- Bedrock model access (Claude, Titan)
- S3 bucket creation and access
- S3 Vectors operations

## Troubleshooting

### Bedrock Access
Ensure your AWS account has Bedrock enabled and models are accessible in your region.

### S3 Vectors CLI
Install the CLI tool:
```bash
pip install s3vectors-embed-cli
s3vectors-embed --help
```

### Missing Dependencies
```bash
pip install streamlit boto3 pypdf colorama numpy
```

## Author

Naveen Kumar -> https://www.linkedin.com/in/tnaveen-kumar/
