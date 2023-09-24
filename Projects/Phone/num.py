import phonenumbers
from phonenumbers import timezone, geocoder , carrier 

num = input("Enter your number : ")
phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
provider = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone , "en")
print(phone)
print(timezone)
print(provider)
print(reg)