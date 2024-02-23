import phonenumbers
from phonenumbers import geocoder

phone =  input('Input phone number in this format: +555512345678: ')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))