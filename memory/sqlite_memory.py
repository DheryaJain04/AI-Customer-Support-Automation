import sqlite3

# Connect to SQLite database
connection = sqlite3.connect(
    "memory/chat_memory.db",
    check_same_thread=False
)

cursor = connection.cursor()

# Create conversation table
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
id INTEGER PRIMARY KEY AUTOINCREMENT,
query TEXT,
intent TEXT,
department TEXT,
response TEXT
)
""")
connection.commit()


# Save conversation
def save_conversation(query, intent, department, response):

    cursor.execute(
        """
        INSERT INTO conversations
        (query, intent, department, response)
        VALUES (?, ?, ?, ?)
        """,
        (
            query,
            intent,
            department,
            response
        )
    )
    connection.commit()


# Retrieve recent conversations
def get_conversation_history(limit=5):
    cursor.execute(
        """
        SELECT query, response
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    if not rows:
        return ""

    rows.reverse()

    history = ""

    for i, row in enumerate(rows, start=1):
        history += f"""
Conversation {i}

User:
{row[0]}

Assistant:
{row[1]}

-------------------------
"""

    return history