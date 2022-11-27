# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

    # Вариант №1

# num = input('Введите вещественное число: ')
# suma = 0

# for digit in num:
#     if digit.isdigit():
#         suma += int(digit)
# print(suma)

    # Вариант №2

# num = input('Введите вещественное число: ')
# num_1 = num.replace(',' , '.')
# num_2 = num_1.split('.')
# num_3 = list(num_2[0] + num_2[1])

# suma = 0
# for i in range(len(num_3)):
#     suma += int(num_3[i])
#     i += 1
# print(suma)

# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))

# factorial = 1
# my_list = []
# for i in range(1, num + 1):
#     my_list.append(factorial)
#     factorial *= (i + 1)
#     i += 1
    
# print(my_list)

# №3 Задайте список из n чисел последовательности (1 + 1\n)^n и выведите на экран их сумму.

# n = int(input('Введите число: '))
# my_list = []

# for i in range(1, n + 1):
#     num = (1 + 1 / i) ** i
#     my_list.append(num)
#     i += 1
# print(my_list)

# print(sum(my_list))

# №4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся одной строкой через пробел.

N = int(input('Введите число: '))
my_list = []

import random
for i in range (N):
    my_list.append(random.randint(-N, N+1))
    i += 1

print(my_list)

# Найдите произведение элементов на указанных пользователем через пробел позициях.

n = input('Введите индексы элементов через пробел: ')

index_list = n.split(' ')

mult = 1
i = 0
chek = True

while i < len(index_list):
    if int(index_list[i]) > len(my_list):
        print('Ошибка!')
        chek = False
        break
    else:
        i += 1
    chek = True    

if chek == True:
    i = 0
    while i < len(index_list):
        mult *= my_list[int(index_list[i])]
        i += 1
    print(mult)

# №6 Реализуйте алгоритм перемешивания списка.

# my_list = list(range(-10,6))

# print(my_list)

# for i in range(round(len(my_list)/2)):
#     if i % 2 == 0:
#         save = my_list[i]
#         my_list[i] = my_list[- i]
#         my_list[- i] = save

# print(my_list)