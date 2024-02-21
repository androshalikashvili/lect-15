import json
from json import JSONEncoder

class Student:
    row_id = 1
    def __init__(self, name, mark, address):
        self.row_id = Student.row_id
        Student.row_id += 1
        self.name = name
        self.mark = mark
        self.address = address


def from_dict_to_student(obj):
    if 'row_id' in obj and 'name' in obj and 'mark' in obj and 'address' in obj:
        return Student(obj.get('row_id'), obj.get('name'), obj.get('mark'), obj.get('address'))
    elif 'sity' in obj and 'street' in obj:
        return Address(obj.get('sity'), obj.get('street'))
    return obj


def st_decode(o):
    return Student(o['name'], o['mark'], o['address'])


class Address:
    def __init__(self, sity, street):
        self.sity = sity
        self.street = street


class StudEncode(JSONEncoder):
    def default(self, o):
        return o.__dict__




#============================================
adr1 = Address("Tbilisi", "Pekini ave. 11")
adr2 = Address("Tbilisi", "Tsereteli ave. 67a")
adr3 = Address("Rustavi", "Meskhishvili str. 15")
adr4 = Address("Rustavi", "Shartava ave. 33")
adr5 = Address("Mtskheta", "Gamsakhurdia str. 12")

st1 = Student("Andria", 87, adr1)
st2 = Student("Mariami", 98, adr2)
st3 = Student("Nino", 99, adr3)
st4 = Student("Dato", 75, adr4)
st5 = Student("Zura", 65, adr5)

json_data = json.dumps([st1, st2, st3, st4, st5], cls=StudEncode, indent=2)

with open("students.json", mode='w', encoding='utf-8') as file:
    file.write(json_data)


# #READ JSON file data
# with open("students.json", mode='r', encoding='utf-8') as file:
#     st_data = json.load(file)

# print(st_data)
# print(type(st_data))

## 2 READ JSON method
with open("students.json", mode='r', encoding='utf-8') as file:
    json_data = file.read()

students = json.loads(json_data, object_hook=from_dict_to_student)    

for student in students:
    if isinstance(student, Student):
        print(f"ID: {student.row_id}, Name: {student.name}, Mark: {student.mark}, Address: {student.address.city}")
    elif isinstance(student, Address):
        print(f"City: {student.city}, Street: {student.street}")


## 3 READ JSON
# st_obj = json.loads(json_data, object_hook=st_decode)


# print(st_obj.row_id, st_obj.name, st_obj.mark, st_obj.address)
# print(st_obj.__dict__)
