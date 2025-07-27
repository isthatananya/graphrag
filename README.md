GraphRAG with LangChain, Neo4j, and Ollama
This project demonstrates a minimal and functional implementation of GraphRAG (Graph-based Retrieval-Augmented Generation) using the LangChain ecosystem, HuggingFace embeddings, Neo4j vector index, and a local language model served by Ollama (Mistral).

Overview
GraphRAG enhances retrieval-augmented generation by storing and retrieving vectorized text chunks from a Neo4j-powered knowledge graph. This example uses:

Neo4jVector for storing embeddings and querying documents.

HuggingFaceEmbeddings for text vectorization.

ChatOllama for running a local LLM (Mistral).

A simple text-based QA system to demonstrate end-to-end functionality.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/isthatananya/graphrag.git
cd graphrag
Create a virtual environment (recommended with Python 3.10):

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate    # On Windows
source .venv/bin/activate # On Unix/Mac
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up the environment variables in a .env file:

ini
Copy
Edit
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password
Replace the URI and credentials with your Neo4j instance settings (use AuraDB or local Neo4j).

Start Ollama and pull the required model:

bash
Copy
Edit
ollama run mistral
Usage
Prepare your document:

Place a sample_text.txt file in the project root.

Run the script:

bash
Copy
Edit
python graphrag_basic.py
This will:

Load the input text.

Chunk and embed the document.

Store embeddings in Neo4j.

Query using a local LLM to answer questions based on the indexed data.

Requirements
Python 3.10

Neo4j Desktop / AuraDB instance

Ollama installed with mistral model pulled

Memory: Minimum 8 GB (for light local inference)

No GPU required (CPU inference using Ollama + small embedding model)

Notes
Uses all-MiniLM-L6-v2 from SentenceTransformers for CPU-friendly embedding.

Ollama must be running in the background with the model loaded.

Neo4j must be active and accessible via the URI provided.

License
MIT
