# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
def Fibonachi():    
    firstNumber = 0
    secondNumber = 1
    count = 1000
    data = open("fib.txt", "w")
    for i in range(count):
        # print(firstNumber, end = " ")
        data.writelines(str(firstNumber) + "\n")
        (firstNumber, secondNumber) = (secondNumber, firstNumber + secondNumber)
# Fibonachi()

# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def Fruits():
    with open("fruits.txt", encoding="utf-8") as data:
        fruits = data.readline().split()
        # print(fruits)
        letter = "П"
        for fruct in fruits:
            if fruct[0] == letter:
                print(fruct)

# Fruits()

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dictionary = \
    {
        'Привет': "Приветик",
        "Как тебя зовут?": "меня зовут Анатолий",
        'Выход': "Пока!"
    }
isStarted = True
while isStarted:
    answer = input("я: ")
    if answer == "Выход":
        isStarted = not isStarted
    if answer in dictionary.keys():
        print("Бот:", dictionary[answer])
    else:
        print("Бот: неизвестная команда")    