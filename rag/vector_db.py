import os
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS

documents = []

document_folder = "rag/documents"

# Load all text documents
for file in os.listdir(document_folder):

    if file.endswith(".txt"):
        loader = TextLoader(
            os.path.join(document_folder, file),
            encoding="utf-8"
        )
        documents.extend(loader.load())

print(f"Loaded {len(documents)} documents.")

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks.")

# Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Build FAISS index
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

# Save vector database
vector_store.save_local("rag/faiss_index")
print("\nVector Database Created Successfully!")