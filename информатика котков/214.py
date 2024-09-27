import time
import random
array = []
start_time = time.time()
for k in range(50000001):
    array.append(k)
print("время заполнения массива: %s seconds " % (time.time() - start_time))



start_time = time.time()
def linear(val, array):
    '''Линейный поиск'''
    for i, x in enumerate(array):
        if x == val:    
            return i
    return -1
print(linear(40099900, array))
print("линейный поиск 		%s seconds " % (time.time() - start_time))



start_time = time.time()
def binary(val, array):
    '''Бинарный поиск'''
    low = 0
    high = len(array)-1
    while low <= high:
        m = low + (high-low)//2
        if array[m] == val:
            return m
        elif array[m] < val:
            low = m+1
        else: 
            high = m-1
    return -1
print(binary(40099900, array))
print("бинарный поиск 		%s seconds " % (time.time() - start_time))



start_time = time.time()
def interpolation(val, array):
    low = 0
    high = len(array)-1
    while low <= high and val >= array[low] and val <= array[high]:
        m = low + (high-low)*(val-array[low])//(array[high]-array[low])
        if array[m] == val:
            return m
        elif array[m] < val:
            low = m+1
        else: 
            high = m-1
    return -1
print(interpolation(40099900, array))
print("интерполяционный поиск 	%s seconds" % (time.time() - start_time))
