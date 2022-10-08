import os
db = "lista.txt"

opcao = str(input("O que vai colocar:\n"))

f = open(db, "r").readlines()
for i in range(len(f)):
	linha = f[i].split()[0]
	converter = f"{linha}|{opcao}"
	print(converter)

	o = open("Lives.txt", "a")
	o.write(converter+"\n")
	o.close()