# Software Architecture task 3 Protocol

In this task I've improved logging-service from the first task using Hazelcast.

Also, I've added a ```tester.py``` and ```tester_get_only.py``` for a quick demo.

## Github URL
https://github.com/maxmyk/software_architecture_microservices/tree/micro_hazelcast

## Task

### Start three instances of logging-service, respectively, three instances of Hazelcast should also be started

Automated via ```run.sh``` script

### Using HTTP POST, write 10 messages msg1-msg10 via facade-service. Show which messages each of the logging-service  instances received (this should be visible in the service logs). Read messages via HTTP GET from facade-service  

See the *first* screenshot.

### Shut down one / two instances of the logging-service (Hazelcast nodes should be shut down along with it) and check if we can read the messages

See the *second* screenshot.

## Screenshots
Ten POST requests "msg1"-"msg10", one GET request and responses to them, and the contents of the console of each microservice.

![screenshot](https://github.com/maxmyk/software_architecture_microservices/blob/micro_hazelcast/screenshot.png?raw=true)

---

GET request with two of the logging services disabled. As we can see, we can read the messages, data is intact.

![screenshot1](https://github.com/maxmyk/software_architecture_microservices/blob/micro_hazelcast/screenshot1.png?raw=true)

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
git checkout micro_hazelcast
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
# Disable 1-2 logging services and then run
python3 tester_get_only.py
```