from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()  # load .env

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

print("🔗 URI:", URI)
print("🧑‍💻 AUTH:", AUTH)

driver = GraphDatabase.driver(URI, auth=AUTH)

try:
    driver.verify_connectivity()
    print("✅ Connected to Neo4j!")
except Exception as e:
    print("❌ Connection failed:", e)
