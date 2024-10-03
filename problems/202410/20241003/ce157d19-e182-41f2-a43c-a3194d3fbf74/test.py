import requests

# url = 'http://host3.dreamhack.games:12285/step2'

# params = {
#     'prev_step_num': '242376424581638458823468578234498040729',
# }

# res = requests.get(url, params=params)

# hidden = '273263523280021926252603376663216422305'

# print(res.text)

url = 'http://host3.dreamhack.games:12285/flag'

data = {
    "param": "pooost",
    "param2": "requeeest",
    "check": "273263523280021926252603376663216422305",
}

res = requests.post(url, data=data)

print(res.text)