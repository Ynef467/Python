# Задача 0. Дано число N. Найти все его делители. Для 
# каждого делителя укажите чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный), 
# 1(нечётный)

from cmath import phase
from itertools import count
import string
from symtable import Symbol
from telnetlib import PRAGMA_HEARTBEAT


def CheckEven(x):
    if x % 2 == 0:
        print(" - чётный")
    else:
        print(" - нечётный")

def Zadacha0():
    number = 60
    for i in range(1, number+1):
        if number % i == 0:
            print(i, end = " ")
            CheckEven(i)

# Zadacha0()


# Задача 1. Выведите таблицу истинности для 
# выражения ¬ X ∨ Y.
      #    не х или y

# Первый вариант

def Istinost():
    for x in range(0, 2):
        for y in range(0, 2):
            sum = x + y
            print(f"{x}, {y}, {sum}")

# Istinost()

# Второй вариант

# print("x| y| ¬ X ∨ Y")
def Istinost1():
    for x in range(0, 2):
        for y in range(0, 2):
            sum = not x or y
            print(f"{x}| {y}|     {int(sum)}")

# Istinost1()

# Задача 2. Напишите программу, в которой 
# пользователь будет задавать две строки, а программа 
# - определять количество вхождений одной строки в 
# другую.
# «qwe» «qwertyqwe» -> 2


def CountSymbols1():
    symbols = 'qwe'
    phrase = 'qwertyqwe'
    count = 0
    lenSymbols = len(symbols)
    lenPrase = len(phrase)
    r = range(0, lenPrase - 2)
    for i in r:
        if symbols == phrase[i:i+lenSymbols]:
            count +=1
    print(count)

# CountSymbols1()

# Четвертый вариант

def CountSymbols2():

    str1 = input('Entter text1: ')
    str2 = input('Entter text2: ')
    print(f'Text1 include Text2 {str1.count(str2)} time(s)')

# def CountSymbols2():

# Задача 3. Дано число N. Заполните список длиной N 
# элементами 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]

def SpisokLenN():

    N = int(input())
    list = [] #- задается пустая строка
    for i in range(0, N):
        list.append((-3)**i) # append - добавляет любое значение в список в конец
    print(list)

# SpisokLenN()
