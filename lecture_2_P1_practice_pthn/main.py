# Пример 1
#a = 5
#print(type(a))
#a = "hello world"
#print(type(a))
#a = 42.0 * 3.141592 / 2.71828
#print(type(a))

# Пример 2
#a = 5
#print(type(a), id(a))
#a = "hello world"
#print(type(a), id(a))
#a = 42.0 * 3.141592 / 2.71828
#print(type(a), id(a))
      
# Пример 3 Функция принимает на вход объект и класс и возвращает истину, если объект
#является экземпляром прямого или косвенного подкласса.
#data = 42
#print(isinstance(data, int))

# Пример 4
#num = 2 + 2 * 2
#digit = 36 / 6
#print(num == digit)
#print(num is digit)

# Пример 5
#a = 5
#print(a, id(a))
#a += 1
#print(a, id(a))

# Пример 6
#txt = 'Hello world!'
#print(txt, id(txt))
#txt = txt.replace(' ', '_')
#print(txt, id(txt))

# Пример 7
#x = 42
#y = 'text'
#z = 3.1415
#print(hash(x), hash(y), hash(z))
#my_list = [x, y, z]
#print(hash(my_list)) # получим ошибку, т.к. list изменяемый

# Example
#print(dir("Hello world!"))
#help("Hello world!")

# Пример 8
#x = int("42")
#y = int(3.1415)
#z = int("hello", base=30)
#print(x, y, z, sep='\n')

# Пример 9 представление в системах
#num = 2 ** 16 - 1
#b = bin(num)
#o = oct(num)
#h = hex(num)
#print(b, o, h)

# Пример 10
# DEFAULT = 42
#num = int(input('Введите уровень или ноль для значения по умолчанию: '))
#level = num or DEFAULT
#print(level)

# Пример 11
#name = input('Как вас зовут? ')
#if name:
    #print('Привет, ' + name)
#else:
    #print('Анонимус, приветствую')

#text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
#print(text)

#Пример 12 Конкатенация строк
#LIMIT = 120
#ATTENTION = 'Внимание!'
#name = input('Твоё имя? ')
#age = int(input('Твой возраст? '))
#text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
#" до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
#print(text)

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())


a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')