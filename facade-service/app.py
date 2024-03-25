# facade_service.py
import sys
from flask import Flask, jsonify, request
import requests
import uuid
import random
import hazelcast

app = Flask(__name__)

print(sys.argv[2:-1])

num_logging_services = int(sys.argv[2])
logging_services_urls = [f"http://localhost:{sys.argv[3 + i]}" for i in range(num_logging_services)]
num_messages_services = int(sys.argv[3 + num_logging_services])
messages_services_ports = sys.argv[4 + num_logging_services:]
messages_services_urls = [f"http://localhost:{port}" for port in messages_services_ports]
cluster_members = [f"172.17.0.1:{int(sys.argv[3 + i]) + 700}" for i in range(num_logging_services)]

print (logging_services_urls)
print (messages_services_urls)
print (cluster_members)
print (messages_services_ports)
# print (f"queue{random.choice(messages_services_ports)}")
client = hazelcast.HazelcastClient(cluster_name="hazelcast-cluster",
    cluster_members=cluster_members,
    lifecycle_listeners=[
        lambda state: print("Prod >>>", state),
    ])

def add_message_to_hazelcast_queue(msg):
    queue = client.get_queue(f"queue{random.choice(messages_services_ports)}")
    while not queue.offer(msg).result():
        pass

@app.route('/post', methods=['POST'])
def post_message():
    msg = request.json['msg']
    unique_id = str(uuid.uuid4())
    payload = {'UUID': unique_id, 'msg': msg}
    
    requests.post(random.choice(logging_services_urls) + "/log", json=payload)
    # adding the message to Hazelcast message queue (producer)
    add_message_to_hazelcast_queue(msg)

    return jsonify({'UUID': unique_id, 'msg': msg}), 200

@app.route('/get', methods=['GET'])
def get_messages():
    print(logging_services_urls)
    logging_response = requests.get(f"{random.choice(logging_services_urls)}/get").json()
    messages_response = requests.get(f"{random.choice(messages_services_urls)}/get").json()
    return jsonify({'logging_service': logging_response, 'messages_service': messages_response}), 200

if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            print("Usage: python app.py <port>")
            sys.exit(1)
        print("LSU", logging_services_urls)
        # Arguments: 5000 3 5001 5002 5003 2 5004 5005
        # I.e. 5000 is the facade-service port, 3 is the number of logging-service instances, 5001 5002 5003 are the logging-service ports,
        # 2 is the number of messages-service instances, 5004 5005 are the messages-service ports
        app.run(host='0.0.0.0', port=int(sys.argv[1]))  #5000)
    finally:
        client.shutdown()
