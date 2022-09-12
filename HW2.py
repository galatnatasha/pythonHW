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

# №3 Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# k = int(input('Введите число: '))
# my_list = []

# for i in range(1, k + 1):
#     num = (1 + 1 / i) ** i
#     my_list.append(num)
#     i += 1
# print(my_list)

# print(sum(my_list))

# №4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].

# N = int(input('Введите число: '))
# my_list = []

# import random
# for i in range (N):
#     my_list.append(random.randint(-N, N))
#     i += 1

# print(my_list)

# # Найдите произведение элементов на указанных пользователем через пробел позициях.

# n = input('Введите индексы элементов через пробел: ')

# index_list = n.split(' ')

# mult = 1
# for i in range(len(index_list)):
#     mult *= my_list[int(index_list[i])]
#     i += 1

# print(mult)

# №6 Реализуйте алгоритм перемешивания списка.

# my_list = list(range(-10,6))

# print(my_list)

# for i in range(round(len(my_list)/2)):
#     if i % 2 == 0:
#         save = my_list[i]
#         my_list[i] = my_list[- i]
#         my_list[- i] = save

# print(my_list)