# 1 Задание с преподователем

# Напишите программу, которая на вход 
# принимает число и выдаёт его квадрат (число умноженное на само себя).

# number = int(input("enter youre number: "))
# print(number * number)
# print(f"{number} * {number} = {number ** 2}")



# 2 Задание с группой

# Напишите программу, которая на вход принимает два 
# числа и проверяет, является ли одно число квадратом 
# другого.
# a = 5; b = 25 -> да 
# a = 9; b = -3 -> да
# a = -3 b = 0 -> нет

# number1 = int(input("enter first number: "))

# number2 = int(input("enter second number: "))
# if number1**2 == number2 or number2**2 == number1:
#     print("yes")

# else:
#     print("no")



# 2 Задание с группой

# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

# number = None
# count = 0
# while number != 0:
#     number = int((input("enter first number: ")))
#     if number % 3 == 0 and number !=0:
#         count += 1
# print("end enter")
# print("kratno 3: ", count)



# 3 Задание с группой

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
        
        # Вариант 1
# numbers = int(input("enter number: "))
# n = range (-numbers, numbers+1)
# print(*n)

        # Вариант 2
# from math import floor

# numbers = float(input("enter number: "))
# x = abs(floor(numbers))
# for i in range(-x, x+1):
#     print(i, end = ' ')



# 4 Задание с группой

# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

        # Вариант 1
# n = float(input("enter number: "))
# fl_part = int(n) - n
# print(abs(int(fl_part * 10)) if int(n) != n else "NO")

        # Вариант 2
# number = input()
# print(number[number.find(".") + 1] if number.find(".") > 0 else -1)



# 5 Задание с группой

# Напишите программу, которая находит наибольшее и наименьшее число из списка значений

        # Вариант 1
# numbers = [int(el) for el in input().split()]
# max_el = min_el = numbers[0]
# for number in numbers:
#     if number > max_el:
#         max_el = number
#     elif number < min_el:
#         min_el = number
# print(*numbers)
# print(f'max = {max_el}')
# print(f'max = {min_el}')

        # Вариант 2
# numbers = [int(el) for el in input().split()]
# print(f'max = {max(numbers)}')
# print(f'min = {min(numbers)}')