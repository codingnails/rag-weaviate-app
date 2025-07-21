from weaviate import Client
from .embedding_client import embedder
import hashlib

def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def store_chunks(client, chunks, source: str):
    collection = client.collections.get("Chunk")

    with collection.batch.fixed_size(batch_size=50) as batch:
        for chunk_text in chunks:
            chunk_hash = compute_hash(chunk_text)
            vector = embedder.embed(chunk_text)

            batch.add_object(
                properties={
                    "text": chunk_text,
                    "source": source,
                    "hash": chunk_hash
                },
                vector=vector
            )

            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break

    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        print(f"First failed object: {failed_objects[0]}")
