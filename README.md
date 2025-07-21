# 📄 PDF-RAG-Weaviate App using Weaviate and OpenAI

A lightweight Retrieval-Augmented Generation (RAG) demo app that transforms any PDF into a smart, searchable knowledge base using Weaviate as a vector store and OpenAI's embedding + generative models.

## 🚀 Features

- 🔍 **PDF Ingestion & Chunking** – Intelligent chunking of PDF documents into searchable text.  
- 🤖 **Semantic Embedding** – Uses `text-embedding-3-small` via `text2vec-openai` module in Weaviate.  
- 🔎 **Semantic Search** – Retrieve relevant text chunks using `near_text` queries.  
- 🧠 **Generative Q&A** – Uses `generative-openai` module to produce contextual answers from retrieved chunks.  
- 📚 **Real-world Use Case** – Example: Troubleshooting legacy appliance manuals, resumes, or academic documents.

## 📄 Sample Data Source

Add any PDF document of your choice to the main folder or specify its path when running the ingestion script. The app will process, chunk, and index the content for semantic search and generative Q&A.
For example, you can try appliance manuals, research papers, reports, or any text-heavy PDFs to build your knowledge base.

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Weaviate** (Local or cloud instance)  
- **OpenAI API** (`text-embedding-3-small`, `gpt-3.5-turbo`) or specify the models you prefer.
- **PyMuPDF (fitz)** – for PDF parsing  
- **dotenv** – for secure API key management

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/codingnails/PDF-RAG-Weaviate.git
cd PDF-RAG-Weaviate
````

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file with your OpenAI key and Weaviate endpoint:

```env
OPENAI_API_KEY=your_openai_key_here
WEAVIATE_URL=https://your-weaviate-endpoint
WEAVIATE_API_KEY=your_weaviate_api_key # if applicable
```

## 📄 Example Usage

### 1. Add a PDF

```bash
python main.py sample.pdf 
```

This will parse, chunk, embed, and store the PDF data in your Weaviate instance.

### 2. Ask Questions

```bash
python main.py
```

Enter natural language questions to get contextual answers from the ingested documents.

## ⚙️ Weaviate Collection Configuration

```python
from weaviate.collections.classes.config import Configure, DataType

client.collections.create(
    name="Chunk",
    properties=[
        {"name": "text", "dataType": DataType.TEXT},
        {"name": "source", "dataType": DataType.TEXT},
        {"name": "hash", "dataType": DataType.TEXT}
    ],
    vectorizer_config=Configure.Vectorizer.text2vec_openai(
        model="text-embedding-3-small"
    ),
    generative_config=Configure.Generative.openai()
)
```

## 🧹 Cleanup

To reset the Weaviate collection:

```python
client.collections.delete("Chunk")
```

## 📌 TODO

* Support multiple PDF uploads
* Build a Streamlit UI for easy Q\&A
* Dockerize the app
* Implement reranking with `rerank-openai`

## 🤝 Acknowledgements

* [Weaviate](https://weaviate.io)
* [OpenAI](https://platform.openai.com)
* [PyMuPDF](https://pymupdf.readthedocs.io)

## 🧑‍💻 Author

**Rupali Gupta**
[LinkedIn](https://www.linkedin.com/in/rupaliguptarg1/) | [GitHub](https://github.com/codingnails)
