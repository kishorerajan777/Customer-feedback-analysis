import mysql.connector
from config import DB_CONFIG

# Establish database connection
def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Insert feedback into the database
def insert_feedback(name, email, feedback, sentiment):
    conn = get_connection()
    if not conn:
        return False  # Return False if connection fails
    
    try:
        with conn.cursor() as cursor:  # Auto-closes cursor
            query = "INSERT INTO feedback (name, email, feedback, sentiment) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, feedback, sentiment))
            conn.commit()
        return True  # Return True if insertion is successful
    except mysql.connector.Error as err:
        print(f"Error inserting feedback: {err}")
        return False
    finally:
        conn.close()

# Fetch all feedback from the database
def fetch_feedback():
    conn = get_connection()
    if not conn:
        return []  # Return empty list if connection fails
    
    try:
        with conn.cursor(dictionary=True) as cursor:  # Auto-closes cursor
            cursor.execute("SELECT * FROM feedback ORDER BY created_at DESC")
            return cursor.fetchall() or []  # Return data or empty list if no records
    except mysql.connector.Error as err:
        print(f"Error fetching feedback: {err}")
        return []
    finally:
        conn.close()
