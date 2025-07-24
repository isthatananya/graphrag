from langchain.embeddings import HuggingFaceEmbeddings

embedder = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "GraphRAG is cool"
embedding = embedder.embed_query(text)

print(embedding[:10])  # print first 10 numbers
