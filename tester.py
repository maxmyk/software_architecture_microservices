# tester.py
import requests

facade_url = "http://localhost:5000"

def test_post_request(msg):
    response = requests.post(f"{facade_url}/post", json={"msg": msg})
    data = response.json()
    
    print("POST Request:")
    print(f"Response Code: {response.status_code}")
    print(f"UUID: {data['UUID']}")
    print(f"Message: {data['msg']}\n")

def test_get_request():
    response = requests.get(f"{facade_url}/get")
    data = response.json()
    
    print("GET Request:")
    print(f"Response Code: {response.status_code}")
    print(f"Logging Service Response: {data['logging_service']}")
    print(f"Messages Service Response: {data['messages_service']}\n")

if __name__ == "__main__":
    test_get_request()
    test_post_request("That's a test message 1.")
    test_get_request()
    test_post_request("That's a test message 2.")
    test_get_request()
    test_post_request("That's a test message 3.")
    test_get_request()
