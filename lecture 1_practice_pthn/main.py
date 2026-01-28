# 1. ЗНАКОМСТВО
#  пример №1:
# print(5, 8, 6)

# пример №2:
# n = 5
# print(n)

# пример №3 (переменная с пустым значением):
# n = None
# print(n)

# пример №4 (дробные переменные):
# n = 1.89
# print(n)

# пример №5 (строковая переменная):
# n = 'Привет мир!'
# n1 = "И привет Катя!"
# print(n, n1)

# пример №6 (тип данных):
# n = 5
# print(type(n))

# пример №7 (вывод значения в кавычках):
# n = 'Hello\'Hello'
# print(n)

# или

# n = '"Hello", "Hello"'
# print(n)

# пример №8 (интерполяция):
# a = 5
# b = 5.89
# c = 'hello'
# print(a, '-', b, '-', c)

# или

# a = 5
# b = 5.89
# c = 'hello'
# print(f"{a} - {b} - {c}")

# или

# a = 5
# b = 5.89
# c = 'hello'
# print("{} - {} - {}".format(a, b, c))

# 2. ВВОД ДАННЫХ INPUT
# пример №1:
# print('Введите первое число:')
# a = input()

# или
# a = input('Введите первое число:')
# b = input('Введите второе число:')
# print(a, '+', b, '=', a + b)
# НЕВЕРНО ПОСЧИТАНО, СЛОЖИЛИСЬ CТРОКИ!!!!!

# ВЕРНОЕ РЕШЕНИЕ
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# print(a, '+', b, '=', a + b)

# пример №2.1:
# приведение типов
# c = 5.89
# print(c)
# n = int(c)
# print(n)

# пример №2.2:
# приведение типов
# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# пример №2.3:
# приведение типов
# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# 3. ОКРУГЛЕНИЕ ЧИСЛА
# пример №1:
# a = 1.43425
# b = 2.2983
# c = round(a * b, 5)
# print(c)

# 4. СОКРАЩЕННЫЕ ОПЕРАТОРЫ ПРИСВАИВАНИЯ
# iter = 2
# iter += 3 # iter = iter + 3 
# iter -= 4 # iter = iter - 4 
# iter *= 5 # iter = iter * 5 
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5 
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# 5. ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'

# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# 6. ЕСЛИ, ИНАЧЕ
# вариант 1
# a = int(input("a = "))
# b = int(input("b = ")) 
# if a > b:
#   print(a) 
# else:
#   print(b)

# вариант 2
# username = input('Введите имя: ')
# if username == 'Маша':
#   print('Ура, это же МАША!')
# elif username == 'Марина':
#   print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар': 
#   print('Ильнар - топ)')
# else:
#   print('Привет, ', username)

# 7. Сложные условия
# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#   print('Число кратно 6')
# if n % 5 == 0 or n % 3 == 0:
#   print('Число кратно 15')

# 8. Цикл WHILE
# поиск суммы цифр числа
# n = 423
# summa = 0
# while n > 0:
#   x = n % 10
#   summa = summa + x
#   n = n // 10
# print(summa) # 9

# 9. Прерывание цикла
# i = 0
# while i < 5:
#   if i == 3:
#      break 
#   i = i + 1
# else:
#   print('Пожалуй') 
#   print('хватит )')
# print(i)

# без break
# n = 423
# summa = 0
# while n > 0:
#   x = n % 10
#   summa = summa + x
#   n = n // 10
# else:
#   print('Пожалуй')
#   print('хватит )')
# print(summa)

# 10. ИСПОЛЬЗОВАНИЕ ФЛАГА
# Найти минимальный делитель
# n = int(input())
# flag = True
# i = 2
# while flag:
#   if n % i == 0: # если остаток при делении числа n на i равен 0
#     flag = False
#     print(i)
#   elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#     print(n)
#     flag = False
#   i += 1

# 11. Цикл FOR
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80 60 40 20
# for i in range(5):
#     print(i)
# # 0 1 2 3 4

# 12. Можно использовать цикл for() и со строками, так как у строк есть нумерация, такая
# же как и у массивов, начинается с 0:

# for i in 'qwerty':
#   print(i)
# q

# w

# e

# r

# t
# y

# или вложенные циклы

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5): 
#        line += "*"
#     print(line)

# 13. Команды для работы со строками:
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'

# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# 14. Срез
# Мы представляем строку в виде массива символов. Значит мы можем
# обращаться к элементам по индексам.
# Отрицательное число в индексе — счёт с конца строки
# print(text[0])                          # c

# print(text[1])                          # ъ

# print(text[len(text)-1])                # к

# print(text[-5])                         # б

# print(text[:])                    # съешь ещё этих мягких французских булок

# print(text[:2])                         # съ

# print(text[len(text)-2:])               # ок

# print(text[2:9])                        # ешь ещё

# print(text[6:-18])                      # ещё этих мягких

# print(text[0:len(text):6])              # сеикакл

# print(text[::6])                        # сеикакл

# text = text[2:9] + text[-5] + text[:2]  # ...
