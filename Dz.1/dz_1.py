# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

number = int(input("enter number: "))

if number == 1:
    print("Понедельник")
elif number == 2:
    print("Вторник")
elif number == 3:
    print("Среда")
elif number == 4:
    print("Четверг")
elif number == 5:
    print("Пятница")
elif number == 6:
   print("Суббота")
elif number == 7:
    print("Воскресенье")
else:
    print("wrong number")