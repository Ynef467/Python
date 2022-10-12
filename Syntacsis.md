Переменные

Типы данных справедливы

int - Целые числа
float - Числа с плавающей точкой
boolean - Логические
str - Строки
list

и др.

int
a = 123

float
b = 1.23

Для того чтобы проверить тип переменной можно ввести следующую команду:
print(type(a))
print(type(b))

Пример в файле lec.py в Lec.1


Разделение с помошью esс последовательностями
s = 'hello \'world'

\' - делает ' без нарушения структуры кода # hello 'world

\n - делает разделене на новую строку # hello 
                                        world



Ввод и вывод данных
print() – отвечает за вывод данных
input() – отвечает за ввод данных



Арифметические операции
Важно и нужно, без них вы не напишете ни одной 
программы
Если помните математику – проблем не будет
+, -, 
*
, /, %, //, 
**
Приоритет операций
**
, ⊕, ⊖, 
*
, /, //, %, +, -
( ) Скобки меняют приоритет


Логические операции
>, >=, <, <=, ==, !=
not, and, or – не путать с &, |, 
^
Кое-что ещё: is, is not, in, not in


Управляющие конструкции: if, if-else

f condition:
    # operator 1
    # operator 2
    # ...
    # operator n
else:
    # operator n + 1
    # operator n + 2
    # ...
    # operator n + m

Управляющие конструкции: if, if-else
   
    if condition1:
 # operator
elif condition2:
 # operator
elif condition3:
 # operator
else:
 # operator



Управляющие конструкции: while
Цикл позволяет выполнить блок операторов какое-то количество раз

 while condition:
 # operator 1
 # operator 2
 # . . .
 # operator n



Управляющие конструкции: while-else

 while condition:
 # operator 1
 # operator 2
 # . . .
 # operator n
else:
 # operator n + 1
 # operator n + 2
 # . . .
 # operator n + m



 Управляющие конструкции: for
 Когда мы знаем, что хотим

 for i in enumeration:
 # operator 1
 # operator 2
 # . . .
 # operator n



Немного о строках

text = 'съешь ещё этих мягких французских булок'
print(len(text))                    # 39
print('ещё' in text)                # True
print(text.isdigit())               # False
print(text.islower())               # True
print(text.replace('ещё','ЕЩЁ'))    #

for c in text:
    print(c)




Немного о строках

text = 'съешь ещё этих мягких французских булок'
print(text[0])                          # c
print(text[1])                          # ъ
print(text[len(text)-1])                # к
print(text[-5])                         # б
print(text[:])                          # print(text)
print(text[:2])                         # съ
print(text[len(text)-2:])               # ок
print(text[2:9])                        # ешь ещё
print(text[6:-18])                      # ещё этих мягких       
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...



Списки: введение
Список – пронумерованная, изменяемая коллекция 
объектов произвольных типов 

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]



Функции
Это фрагмент программы, используемый 
многократно

def function_name(x):
# body line 1
# . . .
# body line n
 # optional return