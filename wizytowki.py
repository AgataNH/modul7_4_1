from faker import Faker
fake = Faker(['pl_PL'])

import datetime

class BaseCard:
   def __init__(self, first_name, last_name, phone, email):
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.email = email

def say_louder(func):
   def wrapper():
       result = func()
       return result
   return wrapper    

@say_louder
def timelength():
    result = end_time - start_time
    return result

def create_contacts(card_number):
    card_list = []
    for _ in range(card_number):
        card = BaseCard(first_name = fake.first_name(), last_name = fake.last_name(), phone = fake.phone_number(), email = fake.email())
        card_list.append(card)
    return card_list

start_time = datetime.datetime.now()

create_contacts(1000)

end_time = datetime.datetime.now()

print(timelength())