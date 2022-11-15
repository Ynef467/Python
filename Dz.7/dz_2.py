# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход 
# подаётся трёхзначное натуральное число. Напишите программу, которая 
# определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.

import random


list = [random.randint(0, 9) for i in range(15)]
print (list)

number = input("Введите число ")

allNumbers = ""
for i in list:
    allNumbers = allNumbers + str(i)
    
print("есть" if allNumbers.count(number) > 0 else "нет")