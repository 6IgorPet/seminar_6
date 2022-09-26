# 3) Задание 4 из второго дз. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Старое решение
n = int(input ("N = "))    
a = int(input ("a = "))
b = int(input ("b = "))
lstN = list(range(n+1))
lst_negative_N = []
for i in lstN:
    k = int(i) * -1
    lst_negative_N.append(k)
    newlist = list(reversed(lst_negative_N))
del newlist[len(newlist)-1]
generalL = newlist + lstN
print(generalL)
mult = generalL [a-1] * generalL [b-1]
print (mult)
 
# Новое решение
def some_f(n, a, b):
    lst = list(range(n+1))
    lst_neg = list(map(lambda x: x*-1, lst)) # map и lambda вместо цикла for
    lst_neg.remove(0)
    lst_neg = list(reversed(lst_neg))
    lst_new = lst_neg + lst
    res = lst_new[a-1] * lst_new[b-1]
    print(lst_new, res)
 
some_f(int(input('N = ')), int(input('a = ')), int(input('b = ')))
 
# 4) Задача 1 из третьего дз. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
 
# Старое решение
elements = input('Введите несколько чисел: ').split()
elem_list = list(elements)[1::2]
print (elem_list)
new_list = [int(i) for i in elem_list]
print (new_list)
print ('Ответ:', sum(new_list))
 
# Новое решение
elements = list(input('Введите несколько чисел: ').split())
print(elements)
res = 0
for i, item in enumerate(elements): # enumerate
    item = int(item)
    if i % 2 == 1:
        res += item
print(res)
 
# Задание 4/ Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.
 
n = int(input('введите целое положительное число N= '))
a = int(input(f'введите позицию первого элемента - от 0 до {n*2}: '))
b = int(input(f'введите позицию второго элемента - от 0 до {n*2}: '))
lst = [i for i in range(-n,n+1)]
print(f'{lst}\n произведение элементов равно: {lst[a]*lst[b]}')
 
 
 
# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая выведет список элементов, 
# стоящих на нечётной позиции.
 
numbers = [2,-3,5,9,3,1]
print([numbers[i] for i in range(len(numbers)) if i % 2 != 0])
 
 
 
#Напишите программу, удаляющую из текста все слова, содержащие 'абв'
 
tex = 'Напишитеабв программу, удаляющую из текстаабв все слова, содержащие "абв"'
print(' '.join((filter(lambda x: 'абв' not in x, tex.split()))))
 
 
 
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов 
# исходной последовательности
 
lst = list(map(int, input("Введите числа через пробел:\n").split()))
new_lst = {lst[i] for i in range(len(lst))}
print(f"Список из неповторяющихся элементов: {new_lst}")