from graph import graph
from memory.sqlite_memory import save_conversation

# Display application header
print("=" * 60)
print("      AI CUSTOMER SUPPORT SYSTEM")
print("=" * 60)

print("\nType 'exit' anytime to quit.\n")

# Keep accepting customer queries until the user exits
while True:

    query = input("Customer: ")

    # Exit the application
    if query.lower() == "exit":
        print("\nThank you for using AI Customer Support!")
        break

    print("\n" + "=" * 60)
    print("Processing Request...")
    print("=" * 60)

    # Execute the LangGraph workflow
    result = graph.invoke(
        {
            "query": query
        }
    )

    # Save the conversation to SQLite memory
    save_conversation(
        result["query"],
        result["intent"],
        result["department"],
        result["response"]
    )

    # Display workflow details
    print("\nDetected Intent :", result["intent"])
    print("Department      :", result["department"])

    if result.get("approval_required"):
        print("Approval Needed : Yes")
    else:
        print("Approval Needed : No")

    # Display the final response after supervisor review
    print("\nFinal Response\n")
    print(result["response"])

    print("\n" + "=" * 60 + "\n")