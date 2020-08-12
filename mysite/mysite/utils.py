import re
import json
from collections import namedtuple

import requests
import requests.cookies
from http.cookies import SimpleCookie
from urllib.parse import urlencode
cookies = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
          }
token = None
response = requests.get(
    'http://b2b.ad.ua/',
    headers=headers
)

if response.status_code == 200:
    for history_response in response.history:
        cookies.update(history_response.cookies)
    cookies.update(response.cookies)
    content = response.text
    print(response.text)
    match = re.search(
        r'<input\s+name="__RequestVerificationToken"\s+type="hidden"\s+value="(?P<value>[a-zA-Z0-9_-]+)"\s*/>',
        content,
    )
    if match:
        token = match.groupdict().get('value')
        pass
    pass

response = requests.post(
    'http://b2b.ad.ua/Account/Login?ReturnUrl=%2F',
    data={
        'ComId': '15',
        'UserName': '10115',
        'Password': 'e89f1a11',
        'RememberMe': False,
        '__RequestVerificationToken': token,
    },
    cookies=cookies,
    headers=headers,
)
if 200 <= response.status_code < 400:
    for history_response in response.history:
        cookies.update(history_response.cookies)
    cookies.update(response.cookies)
    content = response.text
    print(response.text)
else:
    print('Login failed with', response.status_code, response.reason)
    exit(1)
