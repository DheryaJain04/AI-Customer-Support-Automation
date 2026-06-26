from state import SupportState
from rag.retriever import retrieve_context
from llm import llm
from memory.sqlite_memory import get_conversation_history

# Billing Agent
def billing_agent(state: SupportState):

    context = retrieve_context(state["query"])
    history = get_conversation_history()
    state["conversation_history"] = history

    prompt = f"""
You are the Billing Support Agent.

Previous Conversation:
{state["conversation_history"]}

Company Knowledge:
{context}

Current Customer Query:
{state["query"]}

If the previous conversation is useful,
use it.
Otherwise ignore it.
Answer professionally.
"""
    response = llm.invoke(prompt)
    return {
        "response": response.content
    }