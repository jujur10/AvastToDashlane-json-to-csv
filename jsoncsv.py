import json
from time import sleep

temp = []
name = []
url = []
logins = []
passwords = []

nomfichier = input("File name : ")
nomfichierout = input("Name of the output file (without extension): ")
delimiteur = ","

fichier = open(nomfichier, encoding="utf-8", mode="r")
jsonfile = json.load(fichier)
fichier.close()
temp = jsonfile['logins']
for i in range(len(temp)):
	logins.append(temp[i]['loginName'])
for i in range(len(temp)):
	passwords.append(temp[i]['pwd'])
for i in range(len(temp)):
	url.append(temp[i]['url'])
for i in range(len(temp)):
	name.append(temp[i]['custName'])

#print(str(len(logins)) + " " + str(len(passwords))+ " " + str(len(url))+ " " + str(len(name)))

out = open(nomfichierout + ".csv", mode='w')
out.write("name,url,username,password\n")
for i in range(len(logins)):
	out.write(name[i] + delimiteur + url[i] + delimiteur + logins[i] + delimiteur + passwords[i] + '\n')
out.close()
print("Opération réussie !")
sleep(3)