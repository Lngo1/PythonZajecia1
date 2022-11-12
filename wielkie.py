zero= ["  xxx ",
		"x   x",
		"x   x",
		"x   x",
		"x   x",
		"x   x",
		" xxx "]

jeden= ["    xx",
		"  xxxx",
		"xx  xx",
		"    xx",
		"    xx",
		"    xx",
		" xxxxx"]

dwa=   ["  xxx ",
		" x   x",
		"    xx",
		"   xx ",
		"  xx  ",
		" xx   ",
		"xxxxxx"]

trzy=  ["  xxx ",
		"xx  xx",
		"   xx ",
		"  xx  ",
		"   xx ",
		"xx  xx",
		"  xxx "]

cztery=["x   x",
		"x   x",
		"x   x",
		"xxxxx",
		"    x",
		"    x",
		"    x"]

piec=  ["xxxxxx",
		"xx    ",
		"xxxx  ",
		"   xx ",
		"   xx ",
		"   xx ",
		"xxxx  "]

szesc=  ["xxxxx ",
	 	 "xx  x ",
		 "xxxx  ",
		 "x  xx ",
		 "x  xx ",
		 "x  xx ",
		 "xxxx  "]

siedem=["xxxxxx",
		"     x",
		"    x ",
		"   x  ",
		"   x  ",
		"   x  ",
		"   x  "]

osiem= [" xxxx ",
		"x    x",
		"x    x",
		" xxxx ",
		"x    x",
		"x    x",
		" xxxx "]


dziewec=[" xxxx ",
		 "x    x",
		 "x    x",
		 " xxxxx",
		 "     x",
		 "     x",
		 " xxxx "]




a=input("podaj liczbe: ")
for i in range(7):
	tekst_do_wypisania=""
	for j in range(len(a)):
		if a[j]=='0':
			tekst_do_wypisania+=zero[i]
		if a[j]=='1':
			tekst_do_wypisania+=jeden[i]
		if a[j]=='2':
			tekst_do_wypisania+=dwa[i]
		if a[j]=='3':
			tekst_do_wypisania+=trzy[i]
		if a[j]=='4':
			tekst_do_wypisania+=cztery[i]
		if a[j]=='5':
			tekst_do_wypisania+=piec[i]
		if a[j]=='6':
			tekst_do_wypisania+=szesc[i]
		if a[j]=='7':
			tekst_do_wypisania+=siedem[i]
		if a[j]=='8':
			tekst_do_wypisania+=osiem[i]
		if a[j]=='9':
			tekst_do_wypisania+=dziewec[i]

		tekst_do_wypisania+=" "
	print(tekst_do_wypisania)
