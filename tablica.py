def table_start():
	return"<table>\n"
def row_start():
	return"<tr>\n"
def column_function(column):
	return"<td>"+column+"<td>\n"		
def row_end():
	return"</tr>\n"
def table_end():
	return"</table>"

tekst_do_napisania=""
with open("dane.csv") as plik:
	tekst_do_napisania+=table_start()
	for linia in plik:
		tekst_do_napisania+=row_start()
		for column in linia.split(','):
			tekst_do_napisania+=column_function(str(column.rstrip()))
		tekst_do_napisania+=row_end()
	tekst_do_napisania+=table_end()
zapis = open("dane.html","w")
zapis.write(tekst_do_napisania)	
zapis.close()