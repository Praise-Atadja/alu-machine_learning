#!/usr/bin/env python3
"""script that prints the location of a specific user"""
import sys
import requests
import json
import time

def get_user_location(user_api_url):
    try:
        response = requests.get(user_api_url)
        if response.status_code == 200:
            user_data = response.json()
            if 'location' in user_data:
                print("Location:", user_data['location'])
            else:
                print("Location not found for this user.")
        elif response.status_code == 404:
            print("User not found.")
        elif response.status_code == 403:
            reset_time = int(response.headers['X-Ratelimit-Reset'])
            current_time = int(time.time())
            reset_in_minutes = max(0, (reset_time - current_time) // 60)
            print(f"Reset in {reset_in_minutes} min")
        else:
            print("Unexpected error occurred:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_api_url>")
        sys.exit(1)

    user_api_url = sys.argv[1]
    get_user_location(user_api_url)
