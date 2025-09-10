x = int(input("Geben Sie eine ganze Zahl ein: "))
y = int(input("Geben Sie eine zweite ganze Zahl ein: "))

while(y != 0):
	tmp = x % y
	x = y
	y = tmp 

if(x == 1):
	print("Es gibt keinen größten gemeinsamen Teiler (1)...")
else:
	print("Der gesuchte größte gemeinsame Teiler ist:", x)

