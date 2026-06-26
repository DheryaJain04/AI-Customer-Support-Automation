from state import SupportState

# Keywords used for intent detection
sales_keywords = [
    "price",
    "pricing",
    "plan",
    "subscription",
    "product",
    "purchase",
    "buy"
]

technical_keywords = [
    "error",
    "crash",
    "install",
    "login",
    "bug",
    "issue",
    "update"
]

billing_keywords = [
    "refund",
    "payment",
    "invoice",
    "billing",
    "charge",
    "charged",
    "money"
]

account_keywords = [
    "password",
    "profile",
    "account",
    "activate",
    "deactivate",
    "username"
]

memory_keywords = [
    "previous",
    "last",
    "earlier",
    "history",
    "before",
    "previous issue",
    "previous support",
    "last issue",
    "last request",
    "previous request"
]

# Detect the customer's intent based on keywords
def detect_intent(state: SupportState):

    query = state["query"].lower()
    intent = "unknown"
    department = "unknown"

    if any(word in query for word in memory_keywords):
        intent = "memory"
        department = "memory"

    elif any(word in query for word in sales_keywords):
        intent = "sales"
        department = "sales"

    elif any(word in query for word in technical_keywords):
        intent = "technical"
        department = "technical"

    elif any(word in query for word in billing_keywords):
        intent = "billing"
        department = "billing"

    elif any(word in query for word in account_keywords):
        intent = "account"
        department = "account"

    
    return {
        "intent": intent,
        "department": department
    }

# Check whether the customer's request requires manual approval
def check_approval(state: SupportState):

    query = state["query"].lower()

    approval_keywords = [
        "refund",
        "delete account",
        "close account",
        "cancel subscription",
        "cancel my subscription",
        "terminate account",
        "escalate",
        "complaint",
        "compensation",
        "legal",
        "lawsuit"
    ]

    approval_required = any(
        keyword in query
        for keyword in approval_keywords
    )

    return {
        "approval_required": approval_required
    }