import requests
import json

#json from "https://quotes.rest/qod.json"
r = requests.get("https://quotes.rest/qod.json")
res = r.json()
print(json.dumps(res, indent = 4))
#extract contents
q = res['contents']['quotes'][0]
q
print(q['quote'], '\n--', q['author'])
