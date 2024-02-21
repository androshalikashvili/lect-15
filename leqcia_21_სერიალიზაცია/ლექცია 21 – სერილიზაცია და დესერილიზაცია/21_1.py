import json
import pprint

star_wars = """{
"name": "Luke Skywalker",
"height": "172",
"mass": "77",
"hair_color": "blond",
"skin_color": "fair",
"eye_color": "blue",
"birth_year": "19BBY",
"gender": "male",
"alive": true,
"points": [50, 77, 11]
}"""

data = json.loads(star_wars)
# print(data)
# print(type(data))
del data['points']

# json_data = json.dumps(data)
json_data = json.dumps(data, indent=2, sort_keys=True)
# print(json_data)
# # pprint.pprint(json_data)
# print(type(json_data))

with open('states.json', mode='r', encoding='utf-8') as file:
    loader = json.load(file)


for state in loader['states']:
    del state['area_codes']

    print(state)
    # print(state.get('name'), state['abbreviation'])
# print(loader)

with open('test.json', mode='w', encoding='utf-8') as file:
    json.dump(loader, file, indent=2)
