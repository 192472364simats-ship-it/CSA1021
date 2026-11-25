
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host="mysql-service",
        user="root",
        password="root123",
        database="todo_db"
    )

@app.route("/")
def home():
    return jsonify({"message": "Backend is running successfully"})

@app.route("/tasks")
def tasks():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
