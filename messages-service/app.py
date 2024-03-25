# messages_service.py
import sys
from flask import Flask, jsonify
import hazelcast

app = Flask(__name__)

print("a",sys.argv)

cluster_members = [f"172.17.0.1:{int(sys.argv[3 + i])+700}" for i in range(int(sys.argv[2]))]
client = hazelcast.HazelcastClient(cluster_name="hazelcast-cluster",
    cluster_members=cluster_members,
    lifecycle_listeners=[
        lambda state: print("Cons >>>", state),
    ])
messages = []
print(f"queue{sys.argv[1]}")
queue = client.get_queue(f"queue{sys.argv[1]}").blocking()
queue.add_listener(include_value=True, item_added_func=lambda x: print(sys.argv[1], x.item, messages.append(x.item)))

print("Cluster members:")
print(cluster_members)

@app.route('/get', methods=['GET'])
def get_messages():
    print(sys.argv[1],messages)
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    # args:  5005 3 5701 5702 5703
    # I.e. 5005 is the messages-service port, 3 is the number of hazelcast instances, 5701 5702 5703 are the hazelcast ports
    try:
        if len(sys.argv) < 2:
            print("Usage: python app.py <port>")
            sys.exit(1)
        app.run(host='0.0.0.0', port=int(sys.argv[1]))  #5004)
    finally:
        client.shutdown()