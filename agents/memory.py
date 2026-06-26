from state import SupportState
from memory.sqlite_memory import get_conversation_history
from llm import llm


def memory_agent(state: SupportState):

    history = get_conversation_history()

    prompt = f"""
You are a customer support assistant.

Using the previous conversation history below, answer the user's question.

Conversation History:
{history}

Current Question:
{state["query"]}

If the answer exists in the conversation history, answer it.
Otherwise politely say no previous conversation was found.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }