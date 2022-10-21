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


Файлы

Как работать с файлами:
Связать файловую переменную с файлом,
определив модификатор работы
a – открытие для добавления данных
r – открытие для чтения данных
w – открытие для записи данных
w+, r+

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.close()
path = 'file.txt'
data = open(path, 'r')
for line in data: 
    print(line)
data.close()

Это фрагмент программы, используемый 
многократно

def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

def f(x):
    return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType


new file function_file.py

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

import function_file 
print(function_file.f(1)) # Целое
print(function_file.f(2.3)) # 23
print(function_file.f(28)) # None

new file function_file.py
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

import function_file as ff

print(ff.f(1)) # Целое
print(ff.f(2.3)) # 23
print(ff.f(28)) # None


def new_string(symbol, count):

    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # TypeError missing 1 required ...

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
    
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...


Рекурсия?

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

Кортежи

Кортеж – это неизменяемый “список”

t = ()
print(type(t))                      # tuple
t = (1,)
print(type(t))                      # tuple
t = (1)
print(type(t))                      # int
t = (28, 9, 1990)
print(type(t))                      # tuple
colors = ['red', 'green', 'blue']
print(colors)                       # ['red', 'green', 'blue']
t = tuple(colors)
print(t)                            # ('red', 'green', 'blue')


t = tuple(['red', 'green', 'blue'])
print(t[0])                     # red
print(t[2])                     # blue
# print(t[10])                  # IndexError: tuple index out of range
    print(t[-2])                # green
# print(t[-200])                # IndexError: tuple index out of range

for e in t:
    print(e)                    # red green blue
    
t[0] = 'black'                  # TypeError: 'tuple' object does not support item assignment

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue



Словари


Неупорядоченные коллекции произвольных 
объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)           # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])   # ←
# типы ключей могут отличаться


print(dictionary['up']) # ↑
# типы ключей могут отличаться

dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →


Множества

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set


a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}


colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()            # c = {1, 2, 3, 5, 8}
u = a.union(b)          # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)   # i = {8, 2, 5}
dl = a.difference(b)    # dl = {1, 3}
dr = b.difference(a)    # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}


a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})