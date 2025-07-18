from weaviate import Client

def store_chunks(client: Client, chunks, source: str):
    collection = client.collections.get("Chunk")

    objects = [
        {"text": chunk_text, "source": source}
        for chunk_text in chunks
    ]
    

    # Bulk insert all at once
    collection.data.insert_many(objects)

    # print(f"Inserted {len(chunks)} chunks from {source}.")


# def query_similar_chunks(client: Client, query_text: str, limit=3):
#     # Get the collection
#     collection = client.collections.get("Chunk")

#     response = collection.query\
#         .get(properties=["text", "source"])\
#         .with_near_text({"concepts": [query_text]})\
#         .with_limit(limit)\
#         .do()

#     results = response.get("data", {}).get("Get", {}).get("Chunk", [])
#     for idx, res in enumerate(results, 1):
#         text = res.get("text", "[no text]")
#         src = res.get("source", "[no source]")
#         print(f"Result {idx}: {text}  (from: {src})")

    # return results
