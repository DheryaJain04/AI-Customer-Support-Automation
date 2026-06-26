from state import SupportState

# Route the query to the appropriate department
def route_query(state: SupportState):
    return state["department"]

# Decide whether the request requires human approval
def approval_router(state: SupportState):

    if state["approval_required"]:
        return "approval"

    return "supervisor"