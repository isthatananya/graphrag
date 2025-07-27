# GraphRAG

This project demonstrates a minimal and functional implementation of **GraphRAG** (Graph-based Retrieval-Augmented Generation) using:

- **LangChain** for orchestration
- **HuggingFaceEmbeddings** for vectorization
- **Neo4j** as the vector store and knowledge graph backend
- **Ollama (Mistral)** as the local LLM

---

## Overview

GraphRAG enhances retrieval-augmented generation by storing and retrieving vectorized text chunks from a Neo4j-powered knowledge graph.

This example uses:

- `Neo4jVector` for storing embeddings and querying documents
- `HuggingFaceEmbeddings` for text embedding
- `ChatOllama` to run a local model like Mistral

---

## How It Works

1. A sample `.txt` file is loaded and split into chunks
2. Each chunk is embedded using HuggingFace
3. Chunks are stored in a Neo4j vector index
4. A question is passed to the Ollama LLM via LangChain
5. Relevant context is retrieved from Neo4j and passed to the LLM
6. The LLM generates an answer grounded in your document

---

## Requirements

- Python 3.10+
- Neo4j AuraDB or local instance
- Ollama installed locally
- LangChain, HuggingFace, and Neo4j drivers

Install dependencies:

```bash
pip install -r requirements.txt
