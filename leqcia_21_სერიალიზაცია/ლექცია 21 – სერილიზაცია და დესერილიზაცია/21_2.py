import json

with open("states.json", mode='r', encoding='utf-8') as file:
  data = json.load(file)

# print(data['states'])
  
for state in data['states']:
  # print(state)
  del state['area_codes']
  # print(state.get('name'), state['abbreviation'])
  # print(state)

with open('states_new.json', mode='w', encoding='utf-8') as file:
  json.dump(data, file, indent=2)