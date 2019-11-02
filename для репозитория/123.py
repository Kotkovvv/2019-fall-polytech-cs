N = input("введите количество людей в стране ")
N1 = int(N)
a = 0							
b = 0								
c = 0
if (int(N) % 2) == 0:                           
    print(N)
else:
    N=int(N) - 1
while int(N) > 0:
    import random
    r = random.randint(0, 1)
    if r == 0:
        c = c + 1
        a = a + 1

        print("Детей рождено: " + str(a) + " | Из них мальчиков: " + str(b))
    else:
        b = b + 1
        N = int(N) - 2
        a = a + 1
        print("Детей рождено: " + str(a) + " | Из них мальчиков: " + str(b))
N1 = N1 + a
if (N1 % 2) == 0:
    N2 = N1 / 2
else:
    N2 = (N1 - 1) / 2
print("Численность населения после = " + str(N1))
A = (c + N2) / (b + N2)
B = c + N2
C = b + N2
print("отношение количества женщин(" + str(B) +") к мужчинам (" + str(C) +") = " + str(A))
