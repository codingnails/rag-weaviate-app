from weaviate import Client
from .embedding_client import embedder


def query_similar_chunks(client: Client, query_text: str, limit: int = 3):
    collection = client.collections.get("Chunk")
    print(collection.config)

    search_response = collection.query.near_text(
                query=query_text,
                limit=limit,
                return_metadata=['score']
            )

    if not search_response.objects:
        print("No relevant information found. Try rephrasing your question.")
        return None
            
    # Generate response based on found chunks
    response = collection.generate.near_text(
        query=query_text,
        limit=limit,
        grouped_task = (
    f"The following text chunks have been retrieved from a PDF knowledge base in response to a user's query. "
    f"Based on the user's intent, analyze the content and generate a helpful, informative response. "
    f"If applicable, highlight similar experiences, examples, or best practices. Include links if relevant.\n\n"
    f"----- USER QUERY -----\n{query_text}\n----- END QUERY -----\n\n"
    f"Use the retrieved content below to guide your response."))
    
    print("\n🤖 Answer:")
    print(response.generated)


# def query_similar_chunks_with_vector(
#     client: Client,
#     query_text: str,
#     limit: int = 3,
#     collection_name: str = "Chunk"
# ):
#     # Step 1: Embed query text using your OpenAI embedder
#     query_vector = embedder.embed(query_text)

#     # Step 2: Query Weaviate using nearVector with your query vector
#     try:
#         collection = client.collections.get(collection_name)
#         response = collection.query.near_vector(
#             vector=query_vector,
#             limit=limit
#         )

#         for obj in response.objects:
#             print(obj.properties.get("text", "[No text field]"))

#         return response.objects

#     except Exception as e:
#         print(f"Error querying similar chunks: {e}")
#         return None
