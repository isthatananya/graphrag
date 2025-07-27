GraphRAG with LangChain, Neo4j, and Ollama
This project demonstrates a minimal and functional implementation of GraphRAG (Graph-based Retrieval-Augmented Generation) using the LangChain ecosystem, HuggingFace embeddings, Neo4j vector index, and a local language model served by Ollama (Mistral).

Overview
GraphRAG enhances retrieval-augmented generation by storing and retrieving vectorized text chunks from a Neo4j-powered knowledge graph. This example uses:

Neo4jVector for storing embeddings and querying documents.

HuggingFaceEmbeddings for text vectorization.

ChatOllama for running a local LLM (Mistral).

A simple text-based QA system to demonstrate end-to-end functionality.