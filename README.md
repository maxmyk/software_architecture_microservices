# Software Architecture task 1 Protocol

In this task I've implemented 3 microservices: facade-service, logging-service and messages-service using Python and Flask micro web framework.

Also, I've added a ```tester.py``` for a quick demo.

## Github URL
https://github.com/maxmyk/software_architecture_microservices/tree/micro_basics

## Screenshots
POST/GET requests with several messages and responses to them, and the contents of the console of each microservice.

![screenshot](https://github.com/maxmyk/software_architecture_microservices/tree/micro_basics/screenshot.png?raw=true)

### Prerequisites

- Python
    - Flask
    - Requests

### Installation

#### Clone the project

```bash
git clone https://github.com/maxmyk/software_architecture_microservices
cd software_architecture_microservices
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

Run tester
```bash
python3 tester.py
```