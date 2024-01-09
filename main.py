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
f = open('result.html', 'w+', encoding='utf-8')
f.write(loging.text)
f.close()
