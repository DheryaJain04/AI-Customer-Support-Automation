from state import SupportState
from llm import llm

#Unknown Agent
def unknown_agent(state: SupportState):

    prompt = f"""
You are an AI customer support assistant.

The user's query could not be classified into Sales, Billing, Technical Support or Account Support.

User Query:
{state["query"]}

Politely tell the user that you couldn't understand the request and ask them to clarify or rephrase it.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }