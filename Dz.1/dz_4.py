# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

n = int(input('enter youre nomber: '))
string = ""
for n in range(2,n+1,2):
    string += str(n)+", "
print(f'#{n} -> {string}')

