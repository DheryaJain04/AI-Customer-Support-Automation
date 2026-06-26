from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Load embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Load FAISS index
vector_store = FAISS.load_local(
    "rag/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

# Retrieve relevant context
def retrieve_context(query):
    docs = retriever.invoke(query)
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    return context


# Test retriever
if __name__ == "__main__":

    query = input("Enter Query: ")
    context = retrieve_context(query)

    print("\nRetrieved Context\n")
    print("-" * 50)
    print(context)