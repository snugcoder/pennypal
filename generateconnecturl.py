import requests
import json

url = "https://api.finicity.com/connect/v2/generate"

payload = json.dumps({
  "partnerId": "2445584332864",
  "customerId": "7006569567",
  "language": "en",
  "consumerId": "0bf46322c167b562e6cbed9d40e19a4c",
  "redirectUri": "https://www.finicity.com/connect/",
  "webhookContentType": "application/json",
  "webhookData": {},
  "webhookHeaders": {},
  "optionalConsumerInfo": {
    "ssn": "999999999",
    "dob": 1607450357
  },
  "singleUseUrl": True,
  "institutionSettings": {},
  "fromDate": 1607450357,
  "reportCustomFields": [
    {
      "label": "loanID",
      "value": "123456",
      "shown": True
    },
    {
      "label": "loanID",
      "value": "123456",
      "shown": True
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Finicity-App-Token': 'NnAh56fCi25XoO2xofay',
  'Finicity-App-Key': '53ac9ab13d0ad1727aa6b1d326ee957e',
  'Cookie': 'incap_ses_1450_2596171=PKLfHO6Ue2czBFw8EHAfFNdMK2UAAAAAjFOpNYm6x69BezaOFIRXQw==; nlbi_2596171=nWwZNWXy9EVAjsX5pbFNgwAAAAD2zl75wlvC+Dh3OhW1Ng1W; visid_incap_2596171=fpy2peusTIqouEjo1MobAdFLK2UAAAAAQUIPAAAAAACsYh4t5ObeDpvBybYRUkD/'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
