import os
import random
class czlowiek:
	zycie = 0
	exp = 0
	obrazenia = 0
	def __init__(self,klas):
		self.klas=klas

	def info(self):
		print("twoy klas: " +self.klas)
		print("zycie: " +str(self.zycie))
		print("exp: " +str(self.exp))
		print("obrazenia: " +str(self.obrazenia))
	
	def fight(self):
		dmg=random.randint(0,100)
		self.zycie-=dmg
		print("otrzymano obrazenia" +str(self.zycie))
		if self.zycie > 0: 
			print(self.exp+100)
		elif self.zycie== 0:			
			print("Lose")
		else:
			dmg == 0
		self.exp+=1000
		print("wygrales" +str(self.exp))
	




os.system('cls')
print("wyberz klas")

klas1=czlowiek(input("nazwa: "))
klas1.zycie= 100
klas1.exp= 0
klas1.obrazenia = 40 

while(True):
	os.system('cls')
	print("**i-info      **")
	print("**x-wyjscie   **")
	print("**f-walka     **")
	print("**h-leczenie  **")
	a=input("twoje dzialanie: ")
	if a == 'i':
		klas1.info()
	if a == 'x':
		break
	if a == 'f':
		print(klas1.fight())
	if a == 'h':
		klas1.zycie+=20
		print(klas1.zycie)
	input()