from app.weaviate_client import get_client
from ingest.create_class import create_rag_class
from ingest.file_loader import extract_text_from_pdf, chunk_text
from app.embed_store import store_chunks
from app.embedding_client import EmbeddingClient
from app.retriever import query_similar_chunks

def main():
    
    try:

        client = get_client()
        create_rag_class(client)
        #  2. Load PDF & chunk text
        text = extract_text_from_pdf("sample.pdf")
        chunks = chunk_text(text)

        # 3. Store chunks into Weaviate
        store_chunks(client, chunks, source="sample.pdf")

        # 4. Query example
        query_text = "only education place"
        query_similar_chunks(client, query_text)
        client.close()
    except Exception as e:
        print(f"Error creating class: {e}")

   
if __name__ == "__main__":
    main()
