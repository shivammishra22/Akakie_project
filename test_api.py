import requests

# Replace with your actual deployed URL:
BASE_URL = "https://<your-space-name>.hf.space"

def test_email(email_text):
    payload = {"email": email_text}
    resp = requests.post(f"{BASE_URL}/classify", json=payload)
    print("TEST EMAIL:", email_text)
    print("Status Code:", resp.status_code)
    print("Response JSON:", resp.json(), "\n")

if __name__ == "__main__":
    tests = [
        # Basic PII test
        "Hello, John Doe here. My email is john.doe@example.com.",
        # Phone & credit card
        "My phone number is +919876543210 and card is 4111 1111 1111 1111.",
        # No PII
        "I need help with my account settings.",
        # Multiple PII
        "Hi, I'm Alice Smith (alice@foo.com), DOB 12/12/1990, Aadhar 1234-5678-9012."
    ]
    for e in tests:
        test_email(e)
