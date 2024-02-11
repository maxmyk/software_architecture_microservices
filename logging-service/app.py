# logging_service.py
from flask import Flask, jsonify, request

app = Flask(__name__)

messages = {}

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    unique_id = data['UUID']
    msg = data['msg']

    messages[unique_id] = msg
    print(f"Message received: {msg}, UUID: {unique_id}")

    return jsonify({'message': 'Logged successfully'}), 200

@app.route('/get', methods=['GET'])
def get_messages():
    return jsonify(list(messages.values())), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
