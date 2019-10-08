import random
import time
abc = []
dub = []
c = 10000

#поиск повторяющихся элементов
def iteration(abc):
	for j in range(c-1):
		if abc[j] == abc[j+1]:
			dub.append(abc[j])
		else: pass


#Заполнение массива
for i in range(c):
	a = random.randint(3000, 7000)
	abc.append(a)
abc.sort()


start_time = time.time ()
iteration(abc)
print("время поиска = %s секунд" % (time.time() - start_time))


dub.insert(0, "Имеются дубликаты идентификаторов:")
print(dub)
