# 1. Операторы 
# a = 9
# b = 4
# c = -9
#print(a, '//', b, '=', a // b)
#print(c, '//', b, '=', c // b)

# Пример_2
# a = 2
# b = 6
# while a < b:
  # print(a)
  # a += 1

# Пример_3
#a = 5
#print(id(a))
#a = "hello world"
#print(id(a))
#a = 42.0 * 3.141592 / 2.71828
#print(id(a))

# Пример_4
#print(42, sep='___', end='\n(=^.^=)\n')
#print(1, 2, 3, 4, sep='___', end='\n(=^.^=)\n')
#print('Hello', ',', 'world', '!', sep='___', end='\n(=^.^=)\n')

# Пример_5
#number = 42
#print(number, sep='___', end='\n(=^.^=)\n')
#ONE = 1
#TWO = 2
#print(ONE, TWO, 3, 4, sep='> <', end='>')

# Пример_6
#Ввод, функция input()
#name = input('Ваше имя: ')
#if name == 'Маша':
   #print('Ура, это же МАША!')
#elif name == 'Марина':
   #print('Я так ждала Вас, Марина!')
#elif name == 'Ильнар': 
   #print('Ильнар - топ)')
#else:
   #print('Привет, ', name)

# Пример_7
#age = int(input('Ваш возраст сейчас: '))
#how_old = 2023 - age
#print('Год рождения:', '=', how_old )

#or
#age = float(input('Ваш возраст: '))
#how_old = age - 18
#print(how_old, "лет назад ты стал совершеннолетним")

# Пример_8 Антипаттерн магические числа
#ADULT = 18
#age = float(input('Ваш возраст: '))
#how_old = age - ADULT
#print(how_old, "лет назад ты стал совершеннолетним")

# Пример_9 Ветвления
#pwd = 'text'
#res = input('Input password: ')
#if res == pwd:
   #print('Доступ разрешён')

# or

#pwd = 'text'
#res = input('Input password: ')
#if res == pwd:
    #print('Доступ разрешён')
    #print('Но будьте осторожны')
#print('Работа завершена')

# or

#pwd = 'text'
#res = input('Input password: ')
#if res == pwd:
    #print('Доступ разрешён')
    #print('Но будьте осторожны')
#else:
    #print('Доступ запрещён')
#print('Работа завершена')

# or

#pwd = 'text'
#res = input('Input password: ')
#if res == pwd:
    #print('Доступ разрешён')
    #my_math = int(input('2 + 2 = '))
    #if 2 + 2 == my_math:
        #print('Вы в нормальном мире')
    #else:
        #print('Но будьте осторожны')
#else:
    #print('Доступ запрещён')
#print('Работа завершена')


# or

#color = input('Твой любимый цвет: ')
#if color == 'красный':
    #print('Любитель яркого')
#elif color == 'зелёный':
    #print('Ты не охотник?')
#elif color == 'синий':
    #print('Ха, классика!')
#else:
    #print('Тебя не понять')

# Пример_10 Множественное сравнение case, math

#color = input('Твой любимый цвет: ')
#match color:
    #case 'красный' | 'оранжевый':
        #print('Любитель яркого')
    #case 'зелёный':
        #print('Ты не охотник?')
    #case 'синий' | 'голубой':
        #print('Ха, классика!')
    #case _:
        #print('Тебя не понять')

# Пример_11 or, and, not

#А теперь пример кода на Python чтобы разобраться в правильном синтаксисе
#построения логических выражений. Вычислим високосный год в Григорианском
#календаре поэтапно:

#year = int(input('Введите год в формате yyyy: '))
#if year % 4 != 0:
    #print("Обычный")
#elif year % 100 == 0:
    #if year % 400 == 0:
        #print("Високосный")
    #else:
        #print("Обычный")
#else:
    #print("Високосный")

# or

#А теперь выберем все случаи, когда год обычный и запишем их в одну строку:
#if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#print("Обычный")
#else:
#print("Високосный")

# Пример_12 Проверка на вхождение, in

#data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
#num = int(input('Введи число: '))
#if num in data:
    #print('Леонардо передаёт привет!')

#А теперь тот же самый код, но с конструкцией not — отрицание:
#data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
#num = int(input('Введи число: '))
#if num not in data:
   #print('Леонардо грустит :-(')

# Пример_13
# Было:
#my_math = int(input('2 + 2 = '))
#if 2 + 2 == my_math:
   # print('Верно!')
#else:
   # print('Вы уверены?')

# Стало:
#my_math = int(input('2 + 2 = '))
#print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')


# Пример_14 Циклы
#num = float(input('Введите число: '))
#count = 0
#while count < num:
    #print(count)
    #count += 2


# or
#При необходимости работу цикла можно прервать и досрочно вернуться к проверке
#условия. Для этого используем зарезервированное слово continue.
#Выведем все чётные числа (как в прошлом примере), кроме тех, которые кратны 12.

#num = float(input('Введите число: '))
#STEP = 2
#limit = num - STEP
#count = -STEP
#while count < limit:
    #count += STEP
    #if count % 12 == 0:
        #continue
    #print(count)


# or
#Ещё один способ управления циклом — команда break для его досрочного
#завершения. Она отлично подходит для создания циклов с постусловием,
#бесконечных циклов с возможностью выхода.
#Рассмотрим на примере программы, которая просит ввести число внутри заданного
#диапазона.
#min_limit = 0
#max_limit = 10
#while True:
    #print('Введи число между', min_limit, 'и', max_limit, '? ')
    #num = float(input())
    #if num < min_limit or num > max_limit:
       # print('Неверно')
    #else:
        #break
#print('Было введено число ' + str(num))

# Пример_15
# Действие после цикла, else
#min_limit = 0
#max_limit = 10
#count = 3
#while count > 0:
    #print('Попытка ' + str(count))
    #count -= 1
    #num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
    #if num < min_limit or num > max_limit:
        #print('Неверно')
    #else:
        #break

#else:
    #print('Исчерпаны все попытки. Сожалею.')
    #quit()
#print('Было введено число ' + str(num))

# Пример_16
#Цикл итератор for in
#data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
#for item in data:
    #print(item)

# Пример_17
#Для перебора целых чисел цикл for in используется в связке с функцией range().
#num = int(input('Введите число: '))
#for i in range(0, num, 2):
    #print(i)
#p.s.
#range(stop) — перебираем значения от нуля до stop исключительно с шагом один
#range(start, stop) — перебираем значения от start включительно до stop
#исключительно с шагом один
#range(start, stop, step) — перебираем значения от start включительно до stop
#исключительно с шагом step.


# Пример_18
#count = 10
#for i in range(count):
    #for j in range(count):
        #for k in range(count):
            #print(i, j, k)

# Пример_19
#animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
#for animal in animals:
    #print(animal)

# Пример_20
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)



