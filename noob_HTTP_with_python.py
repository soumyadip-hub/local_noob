# -----HTTP WITH PYTHON------
import requests
res = requests.get("https://hackerone.com/opportunities/all")
print(res)
# print(res.headers)
print(res.text)