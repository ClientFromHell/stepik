import requests
import json
from operator import itemgetter

client_id = '60bd82a3a7210b52f902'
client_secret = '98223103429a8ae109cdedba3a2f7423'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
artists = []
with open('dataset_24476_4.txt', 'r') as datafile:
    datafile = datafile.readlines()

    for _ in datafile:
        r = requests.get(f"https://api.artsy.net/api/artists/{_.strip()}", headers=headers)
        j = json.loads(r.text)
        with open('artinfo.txt', 'a') as file:
            file.write(f'{j["sortable_name"]},{j["birthday"]}\n')
            artists.append(f'{j["sortable_name"]},{j["birthday"]}\n'.strip().split(','))

artists = sorted(artists, key=itemgetter(1,0))
for _ in artists:
    print(_[0])


