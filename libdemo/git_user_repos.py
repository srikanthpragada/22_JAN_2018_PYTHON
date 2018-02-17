import requests
import sys

# user = "srikanthpragada"

user = input("Enter git username :")
resp = requests.get('https://api.github.com/users/' + user + "/repos")
if resp.status_code == 404:
     print("Sorry! User not found!")
     sys.exit(0)

repos = resp.json()

if len(repos)== 0:
    print("No repos found!")
    sys.exit(0)


for repo in repos:
    print( repo["name"])
    print( repo["description"])
    print( '-' * 50)







