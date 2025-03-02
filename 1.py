import time
from math import *

def q(n):
    start_time = time.perf_counter()
    if n % 2 == 0:
        a, b = n//2, n//2
        return a, b, time.perf_counter() - start_time
    
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            a = (n // i) * (i - 1)
            b = n // i
            return a, b, time.perf_counter() - start_time


    a = 1
    b = n - 1
    return a, b, time.perf_counter() - start_time

n = int(input("Введите положительное число: "))
while n < 0:
    n = int(input("Вы ввели неверное число. Введите положительное число: "))

max_evc = 1

a, b , timee = q(n)

print(a, b)
print(f"Время: {timee:.6f} сек")

print("""Ломинога Кирилл Юрьевич
090301-ПОВа-О24""")
print("55555555")