from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return jsonify({
        "status": "success",
        "message": "Welcome to API",
        "container_id": hostname
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
