# 30. Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}


a = int(input('Введите число: '))
n = len(input('Введите заданную точность: ').split('.')[1])
print(f'Значение: {a:.{n}f}')



# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N :\n'))
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            print(i)


# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [int(i) for i in input('Введите числа через пробел: ').split()]
def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
print(get_unique_numbers(numbers))


# 33.Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Введите k: "))

def randomlist (k):
    list = []
    for i in range(0, k+1):
        list.append(str(random.randint(0, 100)))
    return list

def ffunc (k, list):
    str_p = ""
    for i in range(k, -1, -1):
        if i != 0:
            if i != 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x^{i} + "
                elif list[i] == 1:
                    str_p += f"x^{i} + "
                else:
                    str_p += ""
            if i == 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x + "
                elif list[i] == 1:
                    str_p += f"x + "
                else:
                    str_p += ""
        else:
            if list[i] != 0:
                str_p += f"{list[i]} = 0"
            else:
                print(len(str_p))
                str_p = str_p[:len(str_p)-2]
                str_p += f"= 0"
    return str_p

list1 = randomlist (k)
list2 = randomlist (k)
ffunc (k, list1)
print (ffunc (k, list1))
ffunc (k, list2)
print (ffunc (k, list2))


f1 = open('ffunc1.txt', 'w')
f1.write(ffunc (k, list1))
f1.close()

f2 = open('ffunc2.txt', 'w')
f2.write(ffunc (k, list2))
f2.close()