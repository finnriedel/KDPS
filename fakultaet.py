num=int(input("Bitte geben sie eine Zahl ein: "))

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

print("Die Fakultät von",num,"ist",fact(num))
