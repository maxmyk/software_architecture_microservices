# tester_get_only.py
import requests

facade_url = "http://localhost:5000"

def test_get_request():
    response = requests.get(f"{facade_url}/get")
    data = response.json()
    
    print("GET Request:")
    print(f"Response Code: {response.status_code}")
    print(f"Logging Service Response: {data['logging_service']}")
    print(f"Messages Service Response: {data['messages_service']}\n")

if __name__ == "__main__":
    test_get_request()
