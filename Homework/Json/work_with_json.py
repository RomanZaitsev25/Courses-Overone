# JSON- JAVASCRIPT OBJECT Notation
import json
from datetime import datetime
from random import randint

str_json = '''
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod"
            }
        ]
    }
}
'''
# будет тип string
print(type(str_json))
# Преоброзование в python файл loads.
data = json.loads(str_json)
print(data)
# будет тип dict
print(type(data))
print(data['response'])
print(type(data['response']))
print(data['response']['items'])
# будет тип список, значит можно итерироваться
print(type(data['response']['items']))
# Расспарсили наш json файл
for item in (data['response']['items']):
    print(item)
    print(item['first_name'], item['last_name'])

# Создадим свой json, на основе имеющиеся.
for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(100, 200)
# преобразуем в метод который поддерживает json
    item['now'] = datetime.now().strftime('%d.%m.%y')
    item['a'] = None
print(data['response']['items'])

# помгает превращать объект в json
new_json = json.dumps(data, indent=2)
print(new_json)
# cохраняем в виде файла
with open('my.json', 'w') as file:
    json.dump(data, file, indent=3)

# что загрузить из файла нам нужно:
with open('my.json', 'r') as file:
    data = json.load(file)
print(data)
print(type(data))
