import requests
# for now (ig) user link will have no input parameters
url = ""

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
