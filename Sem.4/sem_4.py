# Задача 0. Создайте файл random.txt. Запишите в него 
# 10 случайных чисел.

# import random

# numbers = []
# phrase  = 'abcd'
# for i in range(10):
#     numbers.append(random.randint(1, 10))
# print(numbers)

# with open('numbers.txt', 'a') as data:
#     data.writelines(str(numbers) + '\n')
#     data.writelines(phrase + '\n')

# data.close()


# Задача 1. Создайте кортеж, заполненный случайными 
# числами. Напишите метод, который заменяет элемент 
# в кортеже по заданному индексу.

# import random

# size = random.randint(5, 12)
# numbers = tuple(random.randint(10, 100) for i in range(size))
# print(numbers)

# index = int(input("Введите индекс, который необходимо заменить: "))

# numbers = list(numbers)
# numbers[index - 1] = random.randint(10, 100)
# numbers = tuple(numbers)
# print(numbers)



# Задача 2. Актёров разделили на списки по трём качествам 
# «умные», «красивые», «сильные». На главную роль нужен актёр 
# обладающий всеми тремя качествами. Определите, сколько есть 
# претендентов на главную роль. Списки актёров поместите в 
# соответствующие файлы.
# 25 мин
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


def openFile(nameFile):
    f = open(nameFile, encoding='utf-8')
    phrase = f.readlines()
    f.close()
    list = phrase[0].split()
    return set(list)

beauty = openFile('beauty.txt')
strong = openFile('strong.txt')
smart = openFile('smart.txt')

print(beauty.intersection(smart).intersection(strong))