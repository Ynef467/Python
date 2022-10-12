# print("Hello World")

# a = 123

# b = 1.23

# Value = None

# print(type(a))

# print(type(b))

# Value = 798465413

# print(type(Value))

# s = "Hello world"

# print(s)  # Вывод строки

# c = 'hello \'world'
# print(c)
# d = 'hello \nworld'
# print(d)

# print(a, c, d)  # Вывод переменных

# print(a, ' - ', c, ' - ', d)  # Вывод переменных через разделители

# print('{} - {} - {}'.format(a, c, d))  # Вывод переменных через разделители

# print(f'{a} - {c} - {d}')  # Вывод переменных через разделители

# Вывод переменных через разделители в своей последовательности, через index массива
# print('{1} - {2} - {0}'.format(a, c, d))

# f = True
# print(f)

# list = [1, 2, 3]
# print(list)


# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, ' + ' , b, ' = ', a+b) #не получится
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')

# print('Введите а');
# a = int(input()) #добавляем int
# print('Введите b'); 
# b = int(input()) #добавляем int
# print(a, ' + ' , b, ' = ', a+b) #получится

# print('Введите а');
# a = float(input()) #добавляем float для чисел с плавающей точкой
# print('Введите b'); 
# b = float(input()) #добавляем float для чисел с плавающей точкой
# print(a, ' + ' , b, ' = ', a+b)



# a = 123
# b = 321
# c = a+b
# print(c)

# a = 123
# b = -321
# c = a+b
# print(c)

# a = +123
# b = -321
# c = a+b
# print(c)

# a = 2
# b = 8
# c = a-b
# print(c)

# a = 2
# b = 8
# c = a*b
# print(c)

# a = 12
# b = 8
# c = a/b
# print(c)

# a = 12
# b = 5
# c = a // b #Деление в целых числах
# print(c)

# a = 12
# b = 8
# c = a % b #Остаток от деления
# print(c)

# a = 2
# b = 8
# c = a ** b #Возведение в степень
# print(c)

# a = 1.31239196
# b = 3
# c = round(a * b, 5) #Для конкретного колличества знаков после запятой
# print(c)

# a = 3
# a = a + 5
# print(a)

# a = 3
# a += 5
# a *= 5
# print(a)


# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2

# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# a = int(input('a ='))
# b = int(input('b ='))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);

#  username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)



# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)


# for i in 1, 2, 3, 4, 5:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)



# for i in range(1, 4): #порядок до 4
#     print(i)

# for i in range(1, 10, 2): #приращение на 2
#     print(i)

# for i in 'qwe rty':
#     print(i)


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


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