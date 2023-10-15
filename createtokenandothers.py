import requests
import json
import sqlite3

def create_token():
  url = "https://api.finicity.com/aggregation/v2/partners/authentication"

  payload = json.dumps({
    "partnerId": "2445584332864",
    "partnerSecret": "9b3TaYy0akEcOb9OtQTQ"
  })
  headers = {
    'Content-Type': 'application/json',
    'Finicity-App-Key': '53ac9ab13d0ad1727aa6b1d326ee957e',
    'Accept': 'application/json',
    'Cookie': 'incap_ses_1450_2596171=PKLfHO6Ue2czBFw8EHAfFNdMK2UAAAAAjFOpNYm6x69BezaOFIRXQw==; nlbi_2596171=nWwZNWXy9EVAjsX5pbFNgwAAAAD2zl75wlvC+Dh3OhW1Ng1W; visid_incap_2596171=fpy2peusTIqouEjo1MobAdFLK2UAAAAAQUIPAAAAAACsYh4t5ObeDpvBybYRUkD/'
  }
  request = requests.request("POST", url, headers=headers, data=payload)
  print(request.text)
  print(request)
  return request

# adding a customer

def add_customer():

  url = "https://api.finicity.com/aggregation/v2/customers/testing"

  payload = json.dumps({
    "username": "customer_1697336761",
    "firstName": "John",
    "lastName": "Smith"
  })
  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Finicity-App-Key': '53ac9ab13d0ad1727aa6b1d326ee957e',
    'Finicity-App-Token': 'NnAh56fCi25XoO2xofay',
    'Cookie': 'incap_ses_1450_2596171=PKLfHO6Ue2czBFw8EHAfFNdMK2UAAAAAjFOpNYm6x69BezaOFIRXQw==; nlbi_2596171=nWwZNWXy9EVAjsX5pbFNgwAAAAD2zl75wlvC+Dh3OhW1Ng1W; visid_incap_2596171=fpy2peusTIqouEjo1MobAdFLK2UAAAAAQUIPAAAAAACsYh4t5ObeDpvBybYRUkD/'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  if response.status_code == 200:
      customer_data = response.json()
      add_customers_to_db(customer_data)
  else:
    print("Error: Failed to add the customer")

def add_customers_to_db(customer_data):
  conn = sqlite3.connect('pennypal.db')
  cursor = conn.cursor()
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS customers (
          id INTEGER PRIMARY KEY,
          username TEXT,
          firstName TEXT,
          lastName TEXT
      )
  ''')
  cursor.execute("INSERT INTO customers (username, firstName, lastName) VALUES (?, ?, ?)",
                  (customer_data["username"], customer_data["firstName"], customer_data["lastName"]))

    # Commit and close the database connection
  conn.commit()
  conn.close()


# Call the function to add a customer to the Finicity API and insert the data into the SQLite database
#add_customer()

# Generates a URL for the user to connect with 

print(create_token.__builtins__)

def generate_user_link():
  url = "https://api.finicity.com/connect/v2/generate"
  #step 1 of the user guide
  token = create_token()
  
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
    'Finicity-App-Token':  token,
    'Finicity-App-Key': '53ac9ab13d0ad1727aa6b1d326ee957e',
    'Cookie': 'incap_ses_1450_2596171=PKLfHO6Ue2czBFw8EHAfFNdMK2UAAAAAjFOpNYm6x69BezaOFIRXQw==; nlbi_2596171=nWwZNWXy9EVAjsX5pbFNgwAAAAD2zl75wlvC+Dh3OhW1Ng1W; visid_incap_2596171=fpy2peusTIqouEjo1MobAdFLK2UAAAAAQUIPAAAAAACsYh4t5ObeDpvBybYRUkD/'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  return response

#for now commented out
#generate_user_link()


#print(response.text)
# want the user to be able to click the link to be able to authenticate

