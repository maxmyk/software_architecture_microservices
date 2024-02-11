# facade_service.py
from flask import Flask, jsonify, request
import requests
import uuid

app = Flask(__name__)

logging_service_url = "http://localhost:5001"
messages_service_url = "http://localhost:5002"

@app.route('/post', methods=['POST'])
def post_message():
    msg = request.json['msg']
    unique_id = str(uuid.uuid4())
    payload = {'UUID': unique_id, 'msg': msg}
    requests.post(f"{logging_service_url}/log", json=payload)

    return jsonify({'UUID': unique_id, 'msg': msg}), 200

@app.route('/get', methods=['GET'])
def get_messages():
    logging_response = requests.get(f"{logging_service_url}/get").json()
    messages_response = requests.get(f"{messages_service_url}/get").json()
    return jsonify({'logging_service': logging_response, 'messages_service': messages_response}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
