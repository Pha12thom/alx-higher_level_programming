#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html.decode('utf-8'))
