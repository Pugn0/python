import requests
import json
import os

lista = open("db.txt", "r", encoding='utf-8').read().splitlines()
for i in lista:
	cpf = i.split('|')[0]
	nome = i.split('|')[1]
	data_nasc = i.split('|')[2]
	genero = i.split('|')[3]
	email = i.split('|')[4]

	url = 'https://www.allfront.com.br/api/customers'

	cabecalho = {
	'accept': 'application/json, text/plain, */*',
	'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6bnVsbCwiYWRtaW4iOnRydWUsImp0aSI6IjAxYjQxNTRjZjhhNWU0YmZmMDAyODY0YzViYTlmZmNhYjc2NWM4OWIzZTliNGVkOTg0MTg4ZGZjMDU0Nzc3N2IiLCJpYXQiOjE2MDA5ODU3MzQsImV4cCI6MTY1MDU3OTMzNCwiZW1haWwiOiJldmVydG9uQHByZWNvZGUuY29tLmJyIiwiZW1wcmVzYSI6bnVsbCwic2NoZW1hIjoiTGVvbmZlcnNob3AiLCJpZFNjaGVtYSI6NDEsImlkU2VsbGVyIjoiNDMiLCJpZFVzZXIiOjF9.+zm3E/xmXmRnt5juGo+5/cdvdV/ixuUoNOvDxGR0X+I=',
	'content-type': 'application/json; charset=UTF-8',
	'origin': 'https://www.leonfershop.com.br',
	'referer': 'https://www.leonfershop.com.br/',
	}

	payload = {"nomefantasia":nome,"nomecompanhia":nome,"email":email,"cpfcnpj":cpf,"genre":genero,"profissao":"","senha":"@Pugno123","nascimento":data_nasc}

	r = requests.post(url, headers=cabecalho, json=payload).text

	if '"Type":"Success"' in r:
		print(f"Cadastrado {cpf}|{nome}|{email}")
		o = open("cadastrado.txt", "a")
		o.write(f"{cpf}|{nome}|{genero}|{data_nasc}|{email}\n")

	elif 'Label":"CPF' in r:
		print("CPF já cadastrado")

	elif '"Label":"O e-mail' in r:
		print("Email já cadastrado")
	else:
		print(f"Erro desconhecido: {r}")