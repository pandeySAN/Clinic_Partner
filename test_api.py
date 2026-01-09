import requests
import json

BASE_URL = "http://localhost:8000/api/auth"

# Test Registration
print("Testing Registration...")
register_data = {
    "email": "doctor@clinic.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "1234567890",
    "user_type": "doctor"
}

response = requests.post(f"{BASE_URL}/register/", json=register_data)
print(f"Status Code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

if response.status_code == 201:
    tokens = response.json()['data']['tokens']
    print("\n✅ Registration Successful!")
    
    # Test Login
    print("\n\nTesting Login...")
    login_data = {
        "email": "doctor@clinic.com",
        "password": "SecurePass123!"
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    if response.status_code == 200:
        access_token = response.json()['data']['tokens']['access']
        print("\n✅ Login Successful!")
        
        # Test Protected Route
        print("\n\nTesting Protected Route (Get Profile)...")
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(f"{BASE_URL}/profile/", headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✅ All tests passed!")
