from state import SupportState


def approval_node(state: SupportState):

    # Display approval request for sensitive customer actions
    print("\n" + "=" * 50)
    print("        HUMAN APPROVAL REQUIRED")
    print("=" * 50)

    print(f"\nDepartment : {state['department']}")
    print(f"Intent     : {state['intent']}")

    print("\nCustomer Query:")
    print(state["query"])

    # Get approval from the human operator
    choice = input("\nApprove? (yes/no): ").strip().lower()

    approved = choice in [
        "yes",
        "y",
        "approve",
        "approved"
    ]

    # Update the graph state based on the approval decision
    if approved:
        return {
            "approved": True
        }

    return {
        "approved": False,
        "response": "Your request has not been approved."
    }