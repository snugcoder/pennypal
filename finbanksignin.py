import requests
# change below later to something, idk how yet
url = "Follow Step 4 here => https://mstr.cd/3Z1ekdU"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
