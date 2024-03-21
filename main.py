import requests

print("Welcome to Flight Club.\nWe find the best flight deals and email you.")
user_firstname = input("What is your first name?\n")
user_lastname = input("What is your last name?\n")
user_email = input("What is your email?\n")
user_email_confirmation = input("Type your email again.\n")
if user_email == user_email_confirmation:
  SHEETY_ENDPOINT = "https://api.sheety.co/86094799cb47604d81ca5c35d8a61ff7/flightDeals/users"
  body = {
    "user": {
      "firstName": user_firstname,
      "lastName": user_lastname,
      "email": user_email
    }
  }
  response = requests.post(url=SHEETY_ENDPOINT, json=body)
  response.raise_for_status()
  print("You're in the club!")
  
