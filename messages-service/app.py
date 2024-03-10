# messages_service.py
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_static_message():
    return jsonify({'message': 'messages-service is not implemented yet'}), 200

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python app.py <port>")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(sys.argv[1]))  #5004)
