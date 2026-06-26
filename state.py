from typing import TypedDict

class SupportState(TypedDict):
    query: str
    intent: str
    department: str

    retrieved_context: str
    conversation_history: str
    approval_required: bool
    approved: bool
    response: str