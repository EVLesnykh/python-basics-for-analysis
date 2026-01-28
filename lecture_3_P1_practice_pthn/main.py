# Пример №1
# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]

#new_list = list(other_iterator)

# Пример №2

#my_list = [2, 4, 6, 8, 10, 12]
#print(my_list[0])
#print(my_list[6])

# Пример №3
#a = 42
#b = 'Hello world!'
#c = [1, 3, 5, 7]
#my_list = [None]
#my_list.append(a)
#print(my_list)
#my_list.append(b)
#print(my_list)
#my_list.append(c)
#print(my_list)

# Пример №4
# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# err = my_list.pop(10)

# Пример №4
#my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
#spam = my_list.count(2)
#print(spam)
#eggs = my_list.count(3)
#print(eggs)

# Пример №5
#my_list = [4, 8, 2, 9, 1, 7, 2]
#my_list.sort()
#print(my_list)
#my_list.sort(reverse=True)
#print(my_list)

# Пример №6
#my_list = [4, 8, 2, 9, 1, 7, 2]
#res = reversed(my_list)
#print(type(res), res)
#rev_list = list(reversed(my_list))
#print(rev_list)


# Пример №7
#my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
#print(my_list[2:7:2])
#print(my_list[:7:2])
#print(my_list[2::2])
#print(my_list[2:7:])
#print(my_list[8:3:-1])
#print(my_list[3::])
#print(my_list[:7:])

# Пример №8
#my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
#new_list = my_list
#print(my_list, new_list, sep='\n')
#my_list[2] = 555
#print(my_list, new_list, sep='\n')


# Пример №9
#text# = 'Hello world!'
#print(text[6])
#print(text[3:7])


# Пример №10 реверс строк
#text = 'Hello world!'
#print(text[::-1])

#name = 'Alex'
#age = 12
#text = 'Меня зовут {} и мне {} лет'.format(name, age)
#print(text)

#name = 'Alex'
#age = 12
#text = f'Меня зовут {name} и мне {age} лет'
#print(text)

#pi = 3.1415
#print(f'Число Пи с точностью два знака: {pi:.2f}')
#data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
#for item in data:
#print(f'{item:>10}')
#num = 2 * pi * data[1]
#print(f'{num = :_}')


#link = 'https://habr.com/ru/users/dzhoker1/posts/'
#urls = link.split('/')
#print(urls)
#a, b, c = input('Введите 3 числа через пробел: ').split()
#print(c, b, a)


data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1',
'posts']
url = '/'.join(data)
print(url)