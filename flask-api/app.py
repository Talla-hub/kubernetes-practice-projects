from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Récupération des variables d'environnement
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

@app.route("/")
def home():
    return jsonify({"message": "Flask API running!"})

@app.route("/db")
def check_db():
    conn = connect_db()
    if conn:
        return jsonify({"message": "Database connected!"})
    return jsonify({"error": "Cannot connect to database"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
