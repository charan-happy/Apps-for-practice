from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "todo_db")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

def connect_db():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

@app.route("/")
def home():
    return "🚀 To-Do List Web App Running!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route("/health")
def health():
    return "✅ OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
