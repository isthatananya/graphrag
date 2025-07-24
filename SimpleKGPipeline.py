from neo4j import GraphDatabase
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline

# -------------------------------
# 1. Connect to Neo4j Aura (or local)
# -------------------------------
url = "neo4j+s://neo4j.databases.neo4j.io"
username = "neo4j"
password = "CeI9fhJwGxoHvkOO0d8N6km0JGfI9ypPMVcBJlEE0_Q"
driver = GraphDatabase.driver(url, auth=(username, password))

# -------------------------------
# 2. Set up FREE Embedding model (HuggingFace)
# -------------------------------
embedder = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------------
# 3. Set up FREE LLM (Ollama)
# -------------------------------
llm = Ollama(model="mistral")  # Make sure `ollama run mistral` is active

# -------------------------------
# 4. Define Graph Schema
# -------------------------------
entities = [
    {"label": "Company", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "RiskFactor", "properties": [{"name": "name", "type": "STRING"}]}
]

relations = [
    {"label": "FACES_RISK", "source": "Company", "target": "RiskFactor"}
]

# -------------------------------
# 5. Build the GraphRAG Pipeline
# -------------------------------
pipeline = SimpleKGPipeline(
    driver=driver,
    llm=llm,
    embedder=embedder,
    entities=entities,
    relations=relations,
    enforce_schema="STRICT"
)

print("✅ Pipeline ready!")
