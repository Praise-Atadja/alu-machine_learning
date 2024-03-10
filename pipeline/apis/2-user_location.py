#!/usr/bin/env python3
"""Script for getting user location from GitHub API"""

import sys
import requests
import time


def get_user_location(url):
    """Function to retrieve user location from GitHub API"""

    response = requests.get(url)
    res = response.json()

    if response.status_code == 200:
        return res.get('location', 'Location not available')
    elif response.status_code == 404:
        return 'Not found'
    elif response.status_code == 403:
        limit = int(response.headers.get('X-Ratelimit-Reset', 0))
        start = int(time.time())
        elapsed = int((limit - start) / 60)
        return f'Reset in {elapsed} min'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./2-user_location.py <API_URL>')
        sys.exit(1)

    url = sys.argv[1]
    location = get_user_location(url)
    print(location)
