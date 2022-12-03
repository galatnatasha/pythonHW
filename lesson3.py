# 1. Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора.

# import time

# def my_random(number):
#     a = time.time() * (10 ** 5)
#     # print(a)
#     b = round(a % 1, number)
#     # print(b)
#     c = round(b * (10 ** number))
#     # print(c)
#     return c

# # num = int(input('Введите кол-во символов для числа: '))
# # k = my_random(num)


# def my_random_list(number, long):
#     list = []
#     for i in range(long):
#         k = my_random(number)
#         list.append(k)
#         i += 1
#     return list

# num = int(input('введите кол-во символов числа: '))
# long = int(input('Введите колличество чисел для генерации: '))
# h = my_random_list(num, long)
# print(h)


# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# def searcher(list):
#     num = (input('Введите число, которое необходимо найти: '))
#     list1 = []
#     for i in range(len(list)):
#         if num in list[i]:
#             list1.append(list[i])
#     return list1

# l = ['sdf13', 'fds66', '34']
# print(searcher(l))

# 3. Напишите программу, которая определит позицию второго вхождения строки 
# в списке, либо сообщит, что ее нет. 

def searcher_2(list, m):
    a = list.split(' ')
    reserve_list = []
    for i in range(len(a)):
        if str(m) == a[i]:
            reserve_list.append(i)
    if len(reserve_list) < 2:
        return 'совпадений нет' 
    else:
        return reserve_list[1]
            
list = str(input('Введите текст: '))
m = str(input('Введите строку для поиска: '))
print(searcher_2(list, m))
 



    