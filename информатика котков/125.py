lcg = int(input("введите seed "))
a = 1140671485				
c = 128201163
b = (2**32) // 1000000
def rand(lcg):
	lcg = ((lcg * a + c) % b)
	print ("Нанесённый урон =", lcg)
	return(lcg)
for i in range(2):
	rand(lcg)
