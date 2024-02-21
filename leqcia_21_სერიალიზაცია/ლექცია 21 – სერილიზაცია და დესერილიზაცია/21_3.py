# import json

# class Car:
#   def __init__(self, name, engine, price):
#     self.name = name
#     self.engine = engine
#     self. price = price


# # ================
# car1 = Car("Mazda", 1.5, 3000)
# # json.dumps(car1)
# print(car1)
# # print(car1.__dict__)





import json
from json import JSONEncoder

class Car:
  def __init__(self, name, engine, price):
    self.name = name
    self.engine = engine
    self. price = price


class CarEncode(JSONEncoder):
  def default(self, o):
    return o.__dict__
  

# ლექციის დასრულებიდან 5-10 წუთში გამახსენდა
# რითაც ლამბდა ფუნქცია უნდა შემეცვალა ჩვეულებრივი ფუნქციით
def car_decode(o):
  return Car(o['name'], o['engine'], o['price'])



# ================
car1 = Car("Mazda", 1.5, 3000)
json_car1 = json.dumps(car1, cls=CarEncode, indent=2)
print(json_car1)


# car1_obj = json.loads(json_car1, object_hook=lambda obj: Car(obj['name'],
#                                                              obj['engine'],
#                                                              obj['price']))

car1_obj = json.loads(json_car1, object_hook=car_decode)

print(car1_obj)
print(car1_obj.name, car1_obj.engine)
print(car1_obj.__dict__)