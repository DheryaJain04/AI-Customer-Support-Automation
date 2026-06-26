from state import SupportState
from rag.retriever import retrieve_context
from memory.sqlite_memory import get_conversation_history
from llm import llm

# Technical Agent
def technical_agent(state: SupportState):

    context = retrieve_context(state["query"])
    history = get_conversation_history()
    state["conversation_history"] = history

    prompt = f"""
You are a professional Technical Support Agent.

Previous Conversation:
{state["conversation_history"]}

Technical Knowledge:
{context}

Current Customer Query:
{state["query"]}

Answer ONLY using the technical knowledge provided.
If appropriate, provide troubleshooting steps one by one.
If the previous conversation is useful, use it.
Otherwise ignore it.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }