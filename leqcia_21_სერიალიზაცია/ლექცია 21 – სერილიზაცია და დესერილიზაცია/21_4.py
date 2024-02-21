import json
from json import JSONEncoder

class Student:
  def __init__(self, name, phone, address):
    self.name = name
    self.phone = phone
    self.address = address


class Address:
  def __init__(self, city, street):
    self.city = city
    self.street = street


class StudentEncode(JSONEncoder):
  def default(self, o):
    return o.__dict__


# ==============
adr = Address("Tbilisi", 'Didube')
st1 = Student("Andria", '555 62-31-40', adr)


json_st1 = json.dumps(st1, cls=StudentEncode, indent=2)
print(json_st1)

