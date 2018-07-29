#!/usr/bin/env python3

import unittest
import requests
import json

"""
python3 -m unittest -v
./test_main.py -v
"""

class GitHubLatestTestCase(unittest.TestCase):
    """test for github-latest repo"""

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_get_events_url(self):
        """
        
        """
        url = "https://api.github.com/users/ericrosko"
        response = requests.get(url)

        self.assertTrue(response.ok)

        parsed = json.loads(response.content)
        # print(parsed)

        # this pretty prints it to the terminal so I can read it
        # print(json.dumps(parsed, indent=4, sort_keys=True))

        events_url = parsed['events_url']
        # print(events_url)
        self.assertEqual("https://api.github.com/users/ericrosko/events{/privacy}", events_url)

    def test_events_url_privacy_part_on(self):
        url = "https://api.github.com/users/ericrosko/events{/privacy}"
        response = requests.get(url)

        parsed = json.loads(response.content)

        # this pretty prints it to the terminal so I can read it
        # print(json.dumps(parsed, indent=4, sort_keys=True))

        self.assertEqual("Not Found", parsed['message'])

    def test_events_url_without_privacy_ending(self):
        url = "https://api.github.com/users/ericrosko/events"
        response = requests.get(url)

        parsed = json.loads(response.content)

        # this pretty prints it to the terminal so I can read it
        # print(json.dumps(parsed, indent=4, sort_keys=True))

        # print()
        self.assertEqual("2018-07-24T22:18:48Z", parsed[0]['created_at'])


if __name__ == '__main__':
    unittest.main()
