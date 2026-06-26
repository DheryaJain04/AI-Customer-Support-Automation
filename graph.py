from langgraph.graph import StateGraph, END

from state import SupportState
from nodes import detect_intent, check_approval
from router import route_query, approval_router
from approval import approval_node
from supervisor import supervisor_node

from agents.sales import sales_agent
from agents.technical import technical_agent
from agents.billing import billing_agent
from agents.account import account_agent
from agents.unknown import unknown_agent
from agents.memory import memory_agent

# Create the LangGraph workflow
builder = StateGraph(SupportState)

# Register Nodes
builder.add_node(
    "detect_intent",
    detect_intent
)

builder.add_node(
    "sales",
    sales_agent
)

builder.add_node(
    "technical",
    technical_agent
)

builder.add_node(
    "billing",
    billing_agent
)

builder.add_node(
    "account",
    account_agent
)

builder.add_node(
    "memory",
    memory_agent
)

builder.add_node(
    "unknown",
    unknown_agent
)

builder.add_node(
    "check_approval",
    check_approval
)

builder.add_node(
    "approval",
    approval_node
)

builder.add_node(
    "supervisor",
    supervisor_node
)

# Set the starting point of the workflow
builder.set_entry_point(
    "detect_intent"
)

# Route the customer query to the appropriate department
builder.add_conditional_edges(
    "detect_intent",
    route_query,
    {
        "sales": "sales",
        "technical": "technical",
        "billing": "billing",
        "account": "account",
        "memory": "memory",
        "unknown": "unknown"
    }
)

# All department agents proceed to the approval check
builder.add_edge(
    "billing",
    "check_approval"
)

builder.add_edge(
    "sales",
    "check_approval"
)

builder.add_edge(
    "technical",
    "check_approval"
)

builder.add_edge(
    "account",
    "check_approval"
)

# Unknown requests are directly reviewed by the supervisor
builder.add_edge(
    "unknown",
    "supervisor"
)

builder.add_edge(
    "memory",
    "supervisor"
)

# Decide whether human approval is required
builder.add_conditional_edges(
    "check_approval",
    approval_router,
    {
        "approval": "approval",
        "supervisor": "supervisor"
    }
)

# Approved requests are sent to the supervisor for final review
builder.add_edge(
    "approval",
    "supervisor"
)

# End the workflow after supervisor review
builder.add_edge(
    "supervisor",
    END
)

graph = builder.compile()