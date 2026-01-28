# Задача 1
# Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.

# Решение №1:
# def sumNumbers(n):
#   summa = 0
#   for i in range(1, n + 1):
#     summa += i
#   print(f'Сумма чисел числа n = {summa}')

# print(f'Введите число n:')
# n = int(input()) # 5
# sumNumbers(n) # 15

# Решение №2:
# добавим return (завершает работу функции и возвращает знач-е)
# def sumNumbers(n):
#   summa = 0
#   for i in range(1, n + 1):
#     summa += i
#   return summa

# print(f'Введите число n:')
# n = int(input()) # 5
# print(f'Сумма чисел числа n = {sumNumbers(n)}') # 15

# Задача №2:
# Хотим передать нашей функции множество букв и получить из нее слово
# Напишем функцию, которая будет принимать неограниченное число аргументов

# Решение:
# def sum_str(*args): #c помощью переменной args со звездочкой можно передавть аргументы
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e', 'l'))
# print(sum_str('q','e', 'l', 'r', 'g'))

# МОДУЛЬНОСТЬ
# Задача №1:
# Передать функцию из файла modul1 в файл main.py
# import modul1
# print(modul1.max1(5, 9))

# или записать
# from modul1 import max1
# print(max1(5, 9))

# или записать
# from modul1 import * (* импрортировать все функции из modul1)
# print(max1(5, 9))

# Задача №2:
# Сократить название файла modul1 при передачи данных в файл main.py
# import modul1 as m1
# print(m1.max1(5, 9))

# РЕКУРСИЯ
# Задача №1:
# Вывести последовательность Фибоначчи
# Решение:
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2) 

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# АЛГОРИТМЫ
# СОРТИРОВКА
# Пример №1:
# def quick_sort(array):
#   if len(array) <= 1:
#      return array
#   else:
#       pivot = array[0]
#   less = [i for i in array[1:] if i <= pivot] 
#   greater = [i for i in array[1:] if i > pivot]
#   return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))

# Пример №2:
# Сортировка слиянием
def merge_sort(nums):
  if len(nums) > 1:
      mid = len(nums) // 2
      left = nums[:mid]
      right = nums[mid:]
      merge_sort(left)
      merge_sort(right)
      i = j = k = 0
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
      while i < len(left):
         nums[k] = left[i]
         i += 1
         k += 1
      while j < len(right):
         nums[k] = right[j]
         j += 1
         k += 1
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
