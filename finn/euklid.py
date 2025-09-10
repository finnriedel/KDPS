x = int(input("Geben Sie eine ganze Zahl ein: "))
y = int(input("Geben Sie eine zweite ganze Zahl ein: "))

while(x != y):
	if(x > y):
		x = x-y
	else:
		y = y-x
if(x == 1):
	print("Es gibt keinen größten gemeinsamen Teiler (1)...")
else:
	print("Der gesuchte größte gemeinsame Teiler ist:", x)
