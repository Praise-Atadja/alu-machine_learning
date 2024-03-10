#!/usr/bin/env python3
""" Prints the location of a specific GitHub user. """

import time
import requests
import sys
def print_location():
    """print location of user"""
    url = sys.argv[1]
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        if 'location' in data and data['location']:
            print(data['location'])
        else:
            print("Not found")
    elif response.status_code == 403:
        print("Reset in {} min".format(
            (int(response.headers['X-Ratelimit-Reset']) -
            int(response.headers['X-Ratelimit-Reset']))
        ))

    else:
        print("Not found")


if __name__ == "__main__":
    print_location()

    print_location()