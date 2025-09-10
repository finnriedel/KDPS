import random

geheimzahl = random.randrange(0,100,1)
eingabe = 0
zaehler = 0

while eingabe != geheimzahl and zaehler <= 20:
	eingabe = int(input("Ganze Zahl eingeben: "))

	if eingabe < geheimzahl:
		print("Zahl zu klein")

	if eingabe > geheimzahl:
		print("Zahl zu groß")

	zaehler = zaehler+1

print("---------------------------------------------------")
if zaehler >= 20:
	print("Leider konnte die Zahl nicht in unter 20 Versuchen erraten werden.")
else:
	print("Richtig! Sie haben ", zaehler, " Versuche benötigt.")
print("Nun wird das System versuchen, die Zahl zu erraten.")
print("---------------------------------------------------")

comp_zaehler = 0
min = 0
max = 100
finder = 50

while finder != geheimzahl and zaehler < 25:
	if finder < geheimzahl:
		min = finder

	if finder > geheimzahl:
		max = finder
	
	finder=round(0.5*(min+max))

	comp_zaehler=comp_zaehler+1
	print("My next guess is going to be:", finder)


if comp_zaehler < zaehler:
	print("Der Computer hat", zaehler-comp_zaehler, "Versuche weniger gebraucht um die Geheimzahl zu erraten.")
else:
	print("Wow... Du bist schlauer als ein Computer")
