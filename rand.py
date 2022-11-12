import random
b=random.randint(0,10)
a= ()
while a != b:
	a=int(input('zgadnij liczbe: '))
	if a > b:
		print('liczba mnejsza')
	elif a < b:
		print('liczba wieksa')
	else:
		print("Zgadles horray")
		break 
