a = int( input("Введите количество команд ") )
b = a - 3
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print("количество вариантов распределения всем местам = ", str(fact(a)) )
print("количество вариантов распределения первым местам= ", (fact(a)/fact(b)))
