# 1. Считать строку из набора чисел из файла.
# напишите программу, которая покажет наибольшее и наименьшее число. 
# в качестве символа разделителя используйте пробел. 
# результат записать в конец исходного файла. 

# with open ('file.txt', 'w') as data:      # создали текстовый файл и записали в него информацию
#     data.write('63 76 5 7 0 3 4 678 5\n')

# path = 'file.txt'
# data = open(path, 'r')
# new_line = list(map(int, data.read().split(' ')))
# data.close()

# print(new_line) 

# max_num = max(new_line)
# print(max_num)
# min_num = min(new_line)
# print(min_num)
# print(f'min = {min_num}  max = {max_num}')

# path = 'file.txt'
# data = open(path, 'a')
# data.write(f'max = {max_num}, min = {min_num}')
# data.close()

# 2. Найдите корни квадратного уравнения ax2 + bx + c = 0. получить кортеж

# def disk(a, b, c):
#     d = b ** 2 - 4 * a * c
#     print(d)
#     if d < 0:
#         return "корней нет"
#     elif d == 0:
#         x_1 = - b / 2 * a
#         return(x_1,)
#     else:
#         x_1 = round(((- b - d ** 0.5) / (2 * a)), 2)
#         x_2 = round(((- b + d ** 0.5) / (2 * a)), 2)
#         return (x_1, x_2)

# a = int(input('Введите значения a: '))
# b = int(input('Введите значения b: '))
# c = int(input('Введите значения c: '))

# print(disk(a, b, c))
  



