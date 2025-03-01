import mysql.connector
from config import DB_CONFIG  # Import database credentials

def create_database():
    """Creates the feedback_db database if it does not exist."""
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS feedback_db;")
    print("Database 'feedback_db' created (if not exists).")
    conn.close()

def create_table():
    """Creates the feedback table inside feedback_db."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    table_query = """
    CREATE TABLE IF NOT EXISTS feedback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        feedback TEXT,
        sentiment VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    cursor.execute(table_query)
    print("Table 'feedback' created (if not exists).")
    conn.close()

if __name__ == "__main__":
    create_database()  # Create database
    create_table()  # Create table
