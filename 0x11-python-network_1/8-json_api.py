#!/usr/bin/python3
"""a Python script that takes in a letter and
sends a `POST` request to `http://0.0.0.0:5000/search_user`
with the letter as a parameter."""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': letter}
    r = requests.post(url, data=payload)

    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
