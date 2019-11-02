a = int(input("Введите сумму "))
def Conversion():
	N = a
	date = []
	while N > 0:
		number = N % 10
		if number == 1:
			date.append ("один")
		elif number == 2:
			date.append ("два")
		elif number == 3:
			date.append ("три")
		elif number == 4:
			date.append ("четыре")
		elif number == 5:
			date.append ("пять")
		elif number == 6:
			date.append ("шесть")
		elif number == 7:
			date.append ("семь")
		elif number == 8:
			date.append ("восемь")
		elif number == 9:
			date.append ("девять")
		else:
			date.append ("ноль")
		N //= 10
	date.reverse() 
	date.insert(0, a)
	date.insert(1, ":")
	print(*date, sep = ' ')
Conversion()
