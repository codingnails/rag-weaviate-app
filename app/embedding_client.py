from openai import OpenAI
import os

class EmbeddingClient:
    def __init__(self, model: str = "text-embedding-3-small"):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    def embed(self, text: str) -> list[float]:
        clean_text = text.replace("\n", " ")
        response = self.client.embeddings.create(
            model=self.model,
            input=clean_text
        )
        return response.data[0].embedding

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        texts = [t.replace("\n", " ") for t in texts]
        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )
        return [r.embedding for r in response.data]
embedder = EmbeddingClient()
