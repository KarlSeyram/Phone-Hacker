import phonenumbers
from phonenumbers import geocoder, carrier

number = input("Enter phone number with country code (e.g. +14155552671): ")

try:
    phone_number = phonenumbers.parse(number)
    valid = phonenumbers.is_valid_number(phone_number)
    if valid:
        country = geocoder.description_for_number(phone_number, "en")
        service_provider = carrier.name_for_number(phone_number, "en")
        print(f"Number is valid.")
        print(f"Country/Region: {country}")
        print(f"Carrier: {service_provider}")
    else:
        print("Number is not valid.")
except Exception as e:
    print(f"Error: {e}")