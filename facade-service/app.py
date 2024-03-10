# facade_service.py
import sys
from flask import Flask, jsonify, request
import requests
import uuid
import random

app = Flask(__name__)

print(sys.argv[2:-1])
logging_service_urls = [f"http://localhost:{i}" for i in sys.argv[2:-1]]
messages_service_url = f"http://localhost:{sys.argv[-1]}"

@app.route('/post', methods=['POST'])
def post_message():
    msg = request.json['msg']
    unique_id = str(uuid.uuid4())
    payload = {'UUID': unique_id, 'msg': msg}
    
    requests.post(random.choice(logging_service_urls) + "/log", json=payload)

    return jsonify({'UUID': unique_id, 'msg': msg}), 200

@app.route('/get', methods=['GET'])
def get_messages():
    print(logging_service_urls)
    logging_response = requests.get(f"{random.choice(logging_service_urls)}/get").json()
    messages_response = requests.get(f"{messages_service_url}/get").json()
    return jsonify({'logging_service': logging_response, 'messages_service': messages_response}), 200

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python app.py <port>")
        sys.exit(1)
    print("LSU", logging_service_urls)
    app.run(host='0.0.0.0', port=int(sys.argv[1]))  #5000)
