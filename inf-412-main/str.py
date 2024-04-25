# Работа над строками

s = 'Lorem \tIpsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

print(s)
# первый символ строки
print(s[0])

# длина строки
print('len str', len(s))

# последний символ в строке 2 способа:
print('len str', s[len(s) - 1])

print(s[-1])

# срез на 10 первых символах
print(s[:10])

# срез из 10 символов начиная с 10 (с 10 по 20)
print(s[10:20])

# срез с шагом 2
print(s[10:20:2])
# print(s[::3])

# конкатенация строк
s1 = '11111' + 'as das dasd'
print(s1)

# замена первого символа в строке s на строку s1
s = s1 + s[1:]
print(s)

# создание строки из списка (разделением пробела)
l = ['lorem', 'ipsum', 'simply', 'summy', 'of']
s2 = ' '.join(l)
print(s2)

# разбиение строки s по разделению точки
l2 = s.split('.')
print(l2)

# удаление пробелов с начала строки и с конца
s3 = '      hello, sasha!     '
print(s3, 'len: ', len(s3))
s3 = s3.lstrip()
print(s3, 'len: ', len(s3))
s3 = s3.rstrip()
print(s3, 'len: ', len(s3))

# Учимся создавать КАПС 
s4 = 'remaining essentially unchanged'
print(s4.upper())

# наоборот уменьшение
s5 = 'REMAINING ESSENCIALLY UNCHANGED'
print(s5.lower())

s6 = 'lorem ipsum is simply dummy text of the printing and typesetting industry'
s7 = s6[0].upper()
s6 = s7 + s6[1:]
print(s6)
# Lorem ipsum is simply dummy text of the printing and typesetting industry