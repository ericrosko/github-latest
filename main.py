#!/usr/bin/env python3

import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    url = "https://api.github.com/users/{}".format(username)

    response = requests.get(url)
    parsed = json.loads(response.content)
    events_url = parsed['events_url']

    events_url = events_url.replace('{/privacy}', '')

    print("events_url:", events_url)
    print(type(events_url), events_url)

    response = requests.get(events_url)
    parsed = json.loads(response.content)
    # this pretty prints it to the terminal so I can read it
    # print(json.dumps(parsed, indent=4, sort_keys=True))
    print(parsed[0]['created_at'])
