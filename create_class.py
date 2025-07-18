from weaviate import WeaviateClient
from weaviate.collections.classes.config import Configure, DataType, Property


def create_rag_class(client: WeaviateClient):
    # Check if class exists
    class_names = client.collections.list_all()
    if "Chunk" in class_names:
        print("Class 'Chunk' already exists.")
        return

    # Define and create the class (collection)
    client.collections.create(
        name="Chunk",
        vector_config=[
            Configure.Vectors.text2vec_openai(
                name="default",
                vector_index_config=Configure.VectorIndex.hnsw()
            )
        ],
        properties=[
            Property(name="text", data_type=DataType.TEXT)
        ]
    )
    print("Class 'Chunk' created.")
