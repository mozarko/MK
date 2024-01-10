import requests

datas = {
    'username': 'def',
    'password': 'def'
}
login = '9232260355@mail.ru'
password = 'M124578m'
datas['username'] = login
datas['password'] = password
url = 'https://auctions.aleado.ru/auth/login.php'
s = requests.Session()
loging = s.post(url, data=datas)
with open('result.html', 'w+', encoding='utf-8') as file:
    file.write(loging.text)
with open('result.html', encoding='utf-8') as file:
    content = file.readlines()
for el in content:
    if 'Логин' in el:
        print(f'Вход не выполнен')
    if '/auth/logout.php' in el:
        print(f'Удачный вход')
data_get = {
    'mrk': 'TOYOTA'
}
urL_get = 'https://auctions.aleado.ru/auctions/?p=project/findlots&s&ld'
response = requests.get(urL_get, data=data_get)
with open('toyota.html', 'w+', encoding='utf-8') as file:
    file.write(response.text)
