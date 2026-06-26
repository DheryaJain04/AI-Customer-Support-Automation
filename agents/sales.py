from state import SupportState
from rag.retriever import retrieve_context
from memory.sqlite_memory import get_conversation_history
from llm import llm

# Sales Agent
def sales_agent(state: SupportState):

    context = retrieve_context(state["query"])
    history = get_conversation_history()
    state["conversation_history"] = history

    prompt = f"""
You are a professional Sales Support Agent.

Previous Conversation:
{state["conversation_history"]}

Company Knowledge:
{context}

Current Customer Query:
{state["query"]}

Answer ONLY using the company knowledge.
If the previous conversation is useful, use it.
Otherwise ignore it.
Provide a friendly and professional response.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }