import requests

def test_honeypot():
    url = "http://127.0.0.1:5000/honeypot"  # Replace with your actual endpoint if different
    response = requests.get(url)

    if response.status_code == 200:
        print("Honeypot test passed!")
        print("Response from honeypot endpoint:", response.json())
    else:
        print("Honeypot test failed!")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

if __name__ == "__main__":
    test_honeypot()
