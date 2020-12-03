import requests
import json
key = '4a82a104-316c-4314-b4df-ea5bee374f48'
r = requests.get('https://content.guardianapis.com/search?api-key=4a82a104-316c-4314-b4df-ea5bee374f48')
x = json.loads(r.text)
m = x['response']
n = m["results"]
for j in n:
    print("Titles are: " + str(j["webTitle"] + "\n" + "Web url are: " + str(j["webUrl"]) + "\n\n"))
