import json
from json import JSONEncoder

class Car:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price  = price


class CarEncode(JSONEncoder):
    def default(self, o):
        if isinstance(o, Car):
            return o.__dict__
        return super().default(o)

# def car_decode_json():

car1 = Car("Mazda", 2.0, 3000)
car2 = Car("Toyota", 3.5, 4500)
# json.dump(car1)
json_car1 = json.dumps(car1, cls=CarEncode, indent=2)
json_car2 = json.dumps(car2, cls=CarEncode, indent=2)
# print(json_car1)

with open("car.json", mode='w', encoding='utf-8') as file:
    file.write(json_car1)
    file.write(json_car2)


#JSON ფაილიდან, მონაცემებიდან წაკითხვა
# car1_obj = json.loads(json_car1, object_hook= lambda obj: Car(obj['name'],
#                                                               obj['engine'],
#                                                               obj['price']))
# print(car1_obj.__dict__)
# print(car1_obj.name, car1_obj.engine, car1_obj.price)
# print(type(car1_obj))
