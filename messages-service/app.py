# messages_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_static_message():
    return jsonify({'message': 'messages-service is not implemented yet'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
