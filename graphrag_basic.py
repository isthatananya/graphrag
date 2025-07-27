from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Neo4j credentials from environment
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Step 1: Load document
loader = TextLoader("sample_text.txt")
docs = loader.load()

# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# Step 3: Define embeddings (CPU-friendly)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 4: Connect to Neo4j + store chunks
vectorstore = Neo4jVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    url=NEO4J_URI,  # use `url` not `uri`
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    database=os.getenv("NEO4J_DATABASE", "neo4j"),
    index_name="langchain"
)

# Step 5: Load Ollama LLM
llm = ChatOllama(model="mistral", temperature=0)

# Step 6: Build RetrievalQA chain
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# Step 7: Ask a question
query = "What is this text about?"
result = qa_chain.invoke(query)

# Output result
print("💬 Answer:", result["result"])
print("\n📄 Source Documents:")
for doc in result["source_documents"]:
    print(f" - {doc.metadata.get('source', 'N/A')}: {doc.page_content[:200]}...")