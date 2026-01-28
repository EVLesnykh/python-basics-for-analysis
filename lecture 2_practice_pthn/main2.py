# пример 1
# list_1 = [] # Создание пустого списка
# list_1 = list() # Создание пустого списка
# print(list_1)

# пример 2
# list_1 = [1, 2, 3, 4, 5]
# print(list_1)

# пример 3
# вывод результата без квадратных скобок
# list_1 = [1, 2, 3, 4, 5]
# print(*list_1)

# пример 4
# list_1 = [1, 2, 3, 4, 5]
# for i in list_1:
#     print(i)

# пример 5
# узнаем размер нашего списка
# list_1 = [1, 2, 3, 4, 5]
# print(len(list_1))

# пример 6
# выводим определенный элемент их нашего списка
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0]) # 7

# пример 7
# выводим элемент их нашего списка сконца
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[-1]) #-17

# ДОБАВЛЯЕМ ЗНАЧЕНИЯ В СПИСОК
# list_1 = [1,5]
# print(list_1)
# list_1.append(8)
# print(list_1)

# Пишем программу
# list_1 = []
# print(list_1) # выводим первый результат, смотрим, что получится
# for i in range(5):
#     list_1.append(i) #переменная i принимает значение от 0 до 4х. 
#     print(list_1) # При каждой итеррации цикла будем в наш список будем добавлять значение i

# Основные функции в списках
# 1. Удаление последнего элемента списка функция pop
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# 2. Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# 3. Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # 2 - это позиция в массиве, 11 значение аргумента
# print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                          # 1
# print(list_1[1])                          # 2
# print(list_1[len(list_1)-1])                # 10
# print(list_1[-5])                         # 6
# print(list_1[:])                    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])                         # [1, 2]
# print(list_1[len(list_1)-2:])               #[9, 10]
# print(list_1[2:9])                        # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])                      # []
# print(list_1[0:len(list_1):6])              # [1, 7]
# print(list_1[::6])                        # [1, 7]

# КОРТЕЖ (НЕИЗМЕНЯЕМЫЙ СПИСОК)
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1, )
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
# print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять
# кортеж)

# Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# СЛОВАРИ
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# МНОЖЕСТВА
# Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# ОПЕРАЦИИ СО МНОЖЕСТВАМИ
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()           # c = {1, 2, 3, 5, 8}
# u = a.union(b)         # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b)  # i = {8, 2, 5} dl = a.difference(b)   # dl = {1, 3} dr = b.difference(a)   
# # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Замороженный список
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# СПИСКИ
# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]

# 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# ЗАДАЧА №1:
# Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#   list_1.append(i)
#   print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# ЗАДАЧА №2:
# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# print(list_1)

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]