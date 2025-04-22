import os

def connect_to_database():
    db_password = os.getenv('DB_PASSWORD', 'default_password')
    print(f"Connecting to the database with password: {db_password}")

if __name__ == "__main__":
    print("Starting the application...")
    connect_to_database()
