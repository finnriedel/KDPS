nummer = int(input("Zahl eingeben: "))

#REKURSIV
print("------------ REKURSIV ----------")
def fibonacci_rec(n):
	if n >= 2:
		return fibonacci_rec(n-1)+fibonacci_rec(n-2)
	elif n == 1:
		return 1
	else:
		return 0

print(fibonacci_rec(nummer))
#for i in range(0, nummer+1):
#	print(fibonacci_rec(i))

#ITERATIV
print("----------- ITERATIV -----------")

def fibonacci_it(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1

	n_1 = 0
	n_2 = 1
	for i in range(2, n+1):
		temp = n_1
		n_1 = n_2
		n_2 = temp + n_2
		print(n_2)

fibonacci_it(nummer)

