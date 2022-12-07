# 1. Вычислить число c заданной точностью d

# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
# Вывод: 3.14

# def Pi_(num):
#     import math
#     new_num = num.split('.')
#     a = tuple(new_num[1])
#     pi_num = round(math.pi, len(a))
#     return pi_num

# num = str(input('Задайте точность: '))
# print(Pi_(num))

# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# def Chek(k):
#     list_chek = []
#     for i in range(1, k+1):
#         if k % i == 0:
#             list_chek.append(i)
#     if len(list_chek) > 2:
#         return False
#     else:
#         return True

# def Factor_(N):
#     list_ = []
#     for i in range(2,N+1):
#         if (N % i == 0) and (Chek(i) == True):
#             list_.append(i)
#     return list_

# N = int(input('Введите натуральное число: '))
# print(Factor_(N))

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# def Funk(list_):
#     new_list = []
#     for i in range(len(list_)):
#         a = list_.count(list_[i])
#         if a == 1:
#             new_list.append(list_[i])
#     return new_list

# list_1 = tuple(input('Введите последовательность чисел: '))
# print(Funk(list_1))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

# def Funk_1(k):
#     import random
#     b = (f'{random.randint(0, 101)} * (x ** {k})')
#     if k == 1:
#         return f'{random.randint(0, 101)} * x + {random.randint(0, 101)} = 0'
#     else:
#         return f'{b} + {Funk_1(k - 1)} '

# k = int(input('Введите значение для натуральной степени: '))
# print(Funk_1(k))

# with open ('file_1.txt', 'w') as data:
#     data.write(Funk_1(k))

# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).

# def Funk_1(k):
#     import random
#     b = (f'{random.randint(0, 101)} * (x ** {k})')
#     if k == 1:
#         return f'{random.randint(0, 101)} * x + {random.randint(0, 101)} = 0'
#     else:
#         return f'{b} + {Funk_1(k - 1)} '

# k = int(input('Введите значение для натуральной степени: '))
# l = int(input('Введите значение для натуральной степени: '))
# with open ('file_2.txt', 'w') as data_1:
#     data_1.write(Funk_1(k))

# with open ('file_3.txt', 'w') as data_2:
#     data_2.write(Funk_1(l))

# with open ('file_2.txt', 'r') as data_1:
#     for line in data_1:
#         f = line

# with open ('file_3.txt', 'r') as data_2:
#     for line in data_2:
#         g = line

# s = [int(s) for s in str.split(f) if s.isdigit()]
# m = [int(m) for m in str.split(g) if m.isdigit()]

# new_list = []
# if len(s) > len(m):
#     while len(s) > len(m):
#         m.insert(0, 0)
# else:
#     while len(s) < len(m):
#         s.insert(0, 0)

# for i in range(len(m)):
#     new_list.append(s[i] + m[i])

# l = len(new_list)
# final_list = []
# for i in range(l - 2):
#     if i == l - 3:
#         final_list.append(f'{new_list[i]} * x + {new_list[i + 1]} = {new_list[i + 2]}')
#     else:
#         b = (f'{new_list[i]} * (x ** {l - 2 - i}) + ')
#         final_list.append(b) 

# with open ('file_4.txt', 'w') as data_3:
#     data_3.write(' '.join(final_list))