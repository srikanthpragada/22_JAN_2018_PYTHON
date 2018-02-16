import requests

user = "srikanthpragada"
# resp = requests.get('https://api.github.com/users')
resp = requests.get('http://www.srikanthtechnologies.com/rss.xml')
print(resp.status_code)
print(resp.text)


# users = resp.json()
# for u in users:
#     print(u['login'])





