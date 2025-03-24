import os
import requests
import json

def is_sum_greater_than_ten(num1, num2):
    """Check if the sum of two numbers is greater than ten."""
    return (num1 + num2) > 10

def fetch_data_from_api():
    """Fetch data from an example API and return it as a JSON object."""
    url = "https://example.com/api/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def perform_login():
    """
    Perform login using credentials stored in environment variables.
    Returns True if login is successful.
    """
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")

    if not username or not password:
        raise ValueError("API credentials not set in environment variables.")

    credentials = {"username": username, "password": password}
    response = requests.post("https://example.com/api/login", json=credentials)
    return response.status_code == 200

def calculate_sum():
    """Calculate the sum of several fixed numbers."""
    numbers = [10, 20, 30, 40]
    return sum(numbers)

def main():
    """Main function to handle login and data processing."""
    try:
        if perform_login():
            data = fetch_data_from_api()
            if data:
                for item in data:
                    print(item)
            else:
                print("No data returned from API.")
        else:
            print("Login failed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
