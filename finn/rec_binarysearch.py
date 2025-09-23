sorted_array = [2, 5, 8, 10, 11, 13, 15, 16, 18, 20, 23, 26, 28, 30, 37, 40, 41, 43, 46, 55, 57, 58, 59, 70, 71, 74, 78, 83, 92, 93, 95, 97]
gesuchte_zahl = 57
versuche = 0

def rec_binary_search(array, min, max, gesuchte_zahl):
	#mit round (Runden) braucht er nur 3 Versuche
	i = round((min + max)/2)
	#durch //2 (Ganzzahlige Division) braucht er 5 Versuche
	#i = (min+max)//2
	print("Min",sorted_array[min],"Max:",sorted_array[max],"Trying:",sorted_array[i])
	global versuche 
	versuche+=1	

	if(sorted_array[i] == gesuchte_zahl):
		return i
	elif(sorted_array[i] > gesuchte_zahl):
		return rec_binary_search(array, min, i - 1, gesuchte_zahl)
	else:
		return rec_binary_search(array, i + 1, max, gesuchte_zahl)



print("Gefunden am Platz:", rec_binary_search(sorted_array, 0, len(sorted_array)-1, gesuchte_zahl),"in", versuche,"Versuchen.")

#Eigentlich sollte er ab 2.5 aufrunden, tut er aber erst über 5
print(round(2.49999), round(2.5), round(2.50001), round(2.51))
print(5//2)
