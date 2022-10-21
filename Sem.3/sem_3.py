# Задача 0. Создайте скрипт func и функцию чтения 
# последней строки файла. Вызовите её из скрипта example.


def z1():
    data = open('text.txt')
    print(data)
    print(data.readlines())

#  в терминале вышло вот такое
# ['РњРѕСЂРѕР· Рё СЃРѕР»РЅС†Рµ, РґРµРЅСЊ С‡СѓРґРµСЃС‚РЅС‹Р№']

# Решение в замене кодировки
def z1_1():
    data = open('text.txt', encoding="utf-8")

    print(data)
    print(data.readlines())

# Так же необходимо всегда закрывать поток данных
def z1_2():
    data = open('text.txt', encoding="utf-8")

    print(data)
    print(data.readlines())
    data.close() # закрываем.

# В задаче необходимо вывести последнюю строчку
def z1_3():
    data = open('text.txt', encoding="utf-8")
    print(data)
    text = data.readlines()
    print(text[-1]) # или так: print(text[len(text)-1])
    data.close()

# Теперь нужно вызвать метод, дл яэтого создаём файл examle, 
# присваиваем метод для написанного кода и вызываем его из 
# основного документа Import

# import example

# example.ReadLastRow

# Задача 1. Дан файл, заполненный числами построчно. 
# Считайте файл. Выведите все элементы, стоящие на 
# чётных строках, а потом на нечётных.

def PoiskStrok():
    data = open("text_rows.txt", encoding="utf-8")
    point = data.readlines()
    data.close()
    for i in range(0, len(point), 2):
        if i % 2 == 0:
            print(point[i], end="")
    print()
    for i in range(1, len(point), 2):
        if i % 2 != 0:
            print(point[i], end="")
# PoiskStrok()

# Задача 2. При работе с документацией менеджер допустил 
# ошибку, названия товаров перемешались с ценами. Помогите 
# восстановить документ. Порядковый номер товара совпадает с 
# номером цены.
def Sortirovka():
    text = open("strokaPoStolbcam.txt", encoding="utf-8")
    string = text.readline()
    text.close()

    clothes = []
    price = []
    string = string.split()
    for i in string:
        if i.isdigit():
            price.append(i)
        else:
            clothes.append(i)
    for i in range(len(price)):
        price[i]
        print(clothes[i] + ' ' + price[i])

# Sortirovka()


# Задача 4. Считайте строковые данные из файла. 
# Создайте словарь, содержащий все символы в 
# файле.

def CreateDictionary():
    data = open("StrokovieDanniye.txt", encoding="utf-8")
    string1 =data.read()
    data.close
    new_dictionary = {}
    print(string1)
    for i in string1:
        new_dictionary[i] = i
    print(new_dictionary)

CreateDictionary()