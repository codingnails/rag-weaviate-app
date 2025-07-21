import weaviate
import os
from dotenv import load_dotenv
from weaviate.classes.init import Auth

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_client():
    additional_headers = (
        {"X-OpenAI-Api-Key": OPENAI_API_KEY} if OPENAI_API_KEY else None) 
    if "localhost" in WEAVIATE_URL:
        # Local Weaviate
        client = weaviate.connect_to_local(
            port=8080,
            grpc_port=50051,
            headers=additional_headers
        )
    else:
               # Cloud Weaviate (WCS)
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=WEAVIATE_URL,
            auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
            headers=additional_headers
        )

    return client
