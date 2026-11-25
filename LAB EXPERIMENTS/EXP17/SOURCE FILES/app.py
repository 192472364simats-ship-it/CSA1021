
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to EXP17",
        "project": "Flask API with Docker and Kubernetes",
        "status": "Success"
    })

@app.route('/about')
def about():
    return jsonify({
        "experiment": "EXP17",
        "technology": "Flask, Docker and Kubernetes"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
