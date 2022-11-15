# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 
# и 1, знаменатель которых не превышает 11.
# import math

# result = []
# for i in range(2, 12):  #j/i  i = 7, j = 1,2,3,4,5,6
#     for j in range(1, i):
#         # if match.gcd(i, j) == 1:
#         if i < j and fractions(i, j):
#             result.append(f"{j}/{i}")
# print(result)

num = set()
for i in range(1, 11):
    for j in range(2, 12):
        if i < j and Fraction(i, j):
            x = Fraction(f"{i}/{j}")
            num.append(x)
print(num)