import requests
import json

url = "https://api.finicity.com/aggregation/v1/customers/7006569567/accounts"

payload = json.dumps({})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Finicity-App-Token': 'NnAh56fCi25XoO2xofay',
  'Finicity-App-Key': '53ac9ab13d0ad1727aa6b1d326ee957e',
  'Cookie': 'incap_ses_1450_2596171=PKLfHO6Ue2czBFw8EHAfFNdMK2UAAAAAjFOpNYm6x69BezaOFIRXQw==; nlbi_2596171=nWwZNWXy9EVAjsX5pbFNgwAAAAD2zl75wlvC+Dh3OhW1Ng1W; visid_incap_2596171=fpy2peusTIqouEjo1MobAdFLK2UAAAAAQUIPAAAAAACsYh4t5ObeDpvBybYRUkD/'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
