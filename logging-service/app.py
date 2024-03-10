# logging_service.py
import sys
from flask import Flask, jsonify, request
import hazelcast
import subprocess

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    unique_id = data['UUID']
    msg = data['msg']

    print(f"{sys.argv[2]}: Message received: {msg}, UUID: {unique_id}")
    
    client = hazelcast.HazelcastClient(
        cluster_name="hazelcast-cluster",
        cluster_members=[
            f"172.17.0.1:{int(sys.argv[1])+700}"
        ],
        lifecycle_listeners=[
            lambda state: print(f"{sys.argv[2]} >>>", state),
        ]
    )
    distributed_map = client.get_map("my-distributed-map").blocking()
    print(distributed_map.put(unique_id, msg))
    client.shutdown()
    return jsonify({'message': 'Logged successfully'}), 200

@app.route('/get', methods=['GET'])
def get_messages():
    client = hazelcast.HazelcastClient(
        cluster_name="hazelcast-cluster",
        cluster_members=[
            f"172.17.0.1:{int(sys.argv[1])+700}"
        ],
        lifecycle_listeners=[
            lambda state: print(f"{sys.argv[2]} >>>", state),
        ]
    )
    distributed_map = client.get_map("my-distributed-map").blocking()
    print(distributed_map.values())
    print(distributed_map.key_set())
    data_to_return = list(distributed_map.values())
    client.shutdown()
    return jsonify(data_to_return), 200

if __name__ == '__main__':
    try:
        print(sys.argv)
        if len(sys.argv) != 4:
            print("Usage: python app.py <port> <node name> <hazelcast port>")
            sys.exit(1)
        subprocess.run(["docker", "stop", f"{sys.argv[2]}-hazelcast-node"])
        subprocess.run(["docker", "run", "-itd", "--name", f"{sys.argv[2]}-hazelcast-node", "--rm", "-e", f"HZ_NETWORK_PUBLICADDRESS=172.17.0.1:{int(sys.argv[1])+700}", "-e", "HZ_CLUSTERNAME=hazelcast-cluster", "-p", f"{int(sys.argv[1])+700}:{int(sys.argv[-1])}", "hazelcast/hazelcast:5.3.6"])
        app.run(host='0.0.0.0', port=int(sys.argv[1]))
    finally:
        subprocess.run(["docker", "stop", f"{sys.argv[2]}-hazelcast-node"])