import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*SwigPy.*")
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*swigvarlink.*")
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*SwigPyObject.*")

from weaviate_client import get_client
from create_class import create_rag_class
from file_loader import extract_text_from_pdf, chunk_text
from embed_store import store_chunks

def main():
    
    client = get_client()
    try:
        create_rag_class(client)
    except Exception as e:
        print(f"Error creating class: {e}")

    # 2. Load PDF & chunk text
    sample_pdf = "sample.pdf"  # Replace with your PDF filename
    text = extract_text_from_pdf(sample_pdf)
    chunks = chunk_text(text)

    # 3. Store chunks into Weaviate
    # store_chunks(client, chunks, source=sample_pdf)

    # 4. Query example
    query_text = "Education"
    #query_similar_chunks(client, query_text)
    client.close()
if __name__ == "__main__":
    main()
