# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# def func(list):
#     sum = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             sum += int(list[i])
#     return sum

# list_1 = str(input('Введите числа через пробел: '))
# list_2 = list_1.split(' ')

# print(func(list_2))

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def func_2(list):
#     new_list = []
#     if len(list) % 2 == 0:
#         for i in range(int(len(list) / 2)):
#             new_list.append(int(list[i]) + int(list[-1 - i]))
#     else:
#         for i in range(round(len(list) / 2) + 1):
#             new_list.append(int(list[i]) + int(list[-1 - i]))
#     return new_list

# list_1 = str(input('Введите числа через пробел: '))
# list_2 = list_1.split(' ')

# print(func_2(list_2))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def func_3(list):
#     min = float(list[0]) % 1
#     for i in range(len(list)):
#         if float(list[i]) % 1 < min:
#             min = float(list[i]) % 1 
#     max = float(list[0]) % 1 
#     for i in range(len(list)):
#         if float(list[i]) % 1 > max:
#             max = float(list[i]) % 1 
#     dif = round((max - min), 4)
#     return dif      
        

# list_1 = str(input('Введите вещественные числа через пробел: '))
# list_2 = list_1.split(' ')

# print(func_3(list_2))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def calc(num):
#     new_list = []
#     while num > 0:
#         n = num % 2
#         new_list.append(n)
#         if num % 2 == 1:
#             num = round((num - 1) / 2)
#         else: 
#             num = round(num / 2)
#     new_list.reverse()
#     return new_list

# num = int(input('Введите число: '))
# print(calc(num)) 

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# def feb(num):
#     list = [0, 1, 1]
#     list_1 = []
#     for i in range(1, num-1):
#         list.append(list[i]+list[i+1])
#     for i in range(1, len(list)):
#         list_1.append(list[-i])
#     i = -2
#     while i >= (len(list_1) * (-1)):
#         list_1[i] *= (-1)
#         i -= 2
#     total = list_1 + list
#     return total

# num = int(input('Введите число: '))
# print(feb(num))