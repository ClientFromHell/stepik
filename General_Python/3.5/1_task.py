import requests, json

with open('dataset_24476_3.txt', 'r') as file:
    numbers = file.readlines()
    for number in numbers:
        print('Interesting' if requests.get(f'http://numbersapi.com/{number.strip()}/math?json=true').json()['found'] else 'Boring')




