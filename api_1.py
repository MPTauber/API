#py -3 -m venv api_venv
#api_venv/scripts/activate
#pip install requests

import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

headers = {'Accept': 'application/vnd.github.v3+json'}

r= requests.get(url, headers = headers)

print("Status Code:", r.status_code)

response_dict = r.json()

repo_dicts = response_dict['items']

print("info about each repo")

for repo in repo_dicts:
    print("Name:", repo["name"])
    print("Owner:", repo['owner']['login'])
    print("Stars:", repo['stargazer_count'])
    print("Description:", repo['description'])

#print("Total repos:", response_dict['total_count'])