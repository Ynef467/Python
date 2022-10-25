# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

import math

def CheckNumber(number):
    flag = True
    for i in range(2, math.ceil(math.sqrt(number))):
        flag = bool(number % i)
        if not flag:
            break
    return flag

def FindDiviger(number):
    divigers = []
    for i in range(2, number//2):
        while CheckNumber(i) and number%i==0:
            divigers.append(i)
            number /= i

    print(divigers)

number = 243
FindDiviger(number)