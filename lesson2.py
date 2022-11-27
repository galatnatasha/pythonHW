# Напишите программу, которая на вход принимает число N 
# и выдает последовательность из N членов

# num = int(input('Введите число: '))
# i = 0
# n = 3
# # while i <= num:
# #     print(n, end = (' '))
# #     n = n * (-3)
# #     i += 1

# while i < num:  
#     n = (-3) ** i
#     print(n, end = (' '))
#     i += 1


# Для натурального N создать последовательность 3n+1

# num = int(input('Введите число: '))
# i = 0

# while i <= num:
#     n = 3 * i + 1
#     print(str(i) + ':' + str(n) + ',')
#     i += 1

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа определять колличество вхождений одной строки в другой. 

text1 = input('Введите текст: ')
# text2 = input('Введите искомый элемент: ')
# count = 0

# # print(text1.count(text2))

# for i in range(len(text1) - len(text2) + 1): 
#     if text1[i:len(text2) + i] == text2:
#         count += 1
# print(count)


print(len(text1))