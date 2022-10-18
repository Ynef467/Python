# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def Factorial():
    number = int(input("enter number: "))
    result = list(range(1, number+1))

    for i in range(1, number+1):
        factor = 1
        for j in range(1, i+1):
            factor *= j
        result[i-1] = factor
    print(result)

# Factorial()

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def Istinost():
    print('x | y | z | ¬(X ∧ Y) ∨ Z')
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x} | {y} | {z} | {int(not(x and y) or z)}')

# Istinost()

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def Sovpadenie():
    symbols = input("enter symbols without spaces: ")
    phrase = input("enter phrase: ")
    for sym in symbols:
        print(f'{sym} - {phrase.count(sym)}')

# Sovpadenie()


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

numbers = [2, 3, -3, -2, -1, 0, 1]
steps = 2

print(numbers[:-steps])
print(numbers[-steps:])

numbers = (numbers[-steps:])+(numbers[:-steps])
print(numbers)