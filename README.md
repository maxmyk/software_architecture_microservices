# Software Architecture task 4 Protocol

In this task I've improved messaging-service from the first task using Hazelcast messaging queue.

Also, I've added a ```tester.py``` and ```tester_get_only.py``` for a quick demo.

## Github URL
https://github.com/maxmyk/software_architecture_microservices/tree/micro_mq

## Task

### Start three instances of logging-service, respectively, three instances of Hazelcast should also be started. Run two instances of messages-service (locally they can be run on different ports)

Automated via ```run.sh``` script

### Write 10 messages msg1-msg10 via HTTP POST through facade-service. Show which messages each of the logging-service instances received (this should be visible in the service logs). Show what messages each of the messages-service instances received (this should be visible in the service logs). Call HTTP GET on facade-service several times and get the combined two sets of messages - these should be messages from logging-service and messages-service

See the *first* screenshot.

### Important

As the *second* screenshot shows, both messaging-services received the messages simultaneously. In order to show the different behavior, I've created another implementation that uses separate queues (*first* screenshot).

## Screenshots
Ten POST requests "msg1"-"msg10", one GET request and responses to them, and the contents of the console of each microservice. Then, two additional GET requests to show that messages are distributed

![screenshot](https://github.com/maxmyk/software_architecture_microservices/blob/micro_mq/screenshot.png?raw=true)

---

Same as first, but with one queue.

![screenshot1](https://github.com/maxmyk/software_architecture_microservices/blob/micro_mq/screenshot1.png?raw=true)

---

Distribution of items in two queues.

![screenshot2](https://github.com/maxmyk/software_architecture_microservices/blob/micro_mq/screenshot2.png?raw=true)

---

### Prerequisites

- Python
    - Flask
    - Requests
    - Hazelcast
- Docker

### Installation

#### Clone the project

```bash
git clone https://github.com/maxmyk/software_architecture_microservices
cd software_architecture_microservices
git checkout micro_mq
```

#### Chmod ```run.sh``` for execution

```bash
chmod +x run.sh
```

### Usage
Start the services automatically (tested on Ubuntu 22.04 LTS)
```bash
./run.sh
```
Or start them manually in separate bash windows.

Run testers
```bash
python3 tester.py
python3 tester_get_only.py
```