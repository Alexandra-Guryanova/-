# print('Hello, World!')

print('Hello', 'World!\n') # print Hello World!
print('Hello', 'World!') # print Hello World!
print('Hello', 'World!') # print Hello World!

# print Hello World!
print(
    'Hello',
    'World!'
    )

if 3 > 2:
    print('yes, 3 > 2')

    if 4 > 3:
        print('but 3 < 4')

print('Welcome to Hell')

# print Number of 0 to 10
# for i in range(10):
#     print(i) 

a = 1
b = 2
c = 5.6

s = 'Hello, Katya!'

print(a, b, c, s)

a = 'aaaa'

print('a:', type(a))
print('b:', type(b))
print('c:', type(c))
print('s:', type(s))

b = float(b)
c = str(c)
d = int(2.7)

print('b:', type(b), b)
print('c:', type(c), c)
print('d:', type(d), d)

print(a is b) 
# сравнивает переменные по их типу данных

l = [1, 2, 3, 'b', 'c', 5.2]
print(l[0])
# первый элемент
print(len(l))
# функция определения сколько элементов в списке
print(l[len(l)-1])
# функция выдает последний элемент

l.append('hi')
# добавляет элемент в конец списка
print(l)

if 1 > 2:
    print('1 > 2')
else:
    print ('2 > 1')

if 1 > 2:
    print('1 > 2')
elif 1 > 0.5:
    print('1 > 0.5')
else:
    print('1 < 2 and 1 < 0.5')

def sum(a, b):
    if type(a) == str or type(b) == str:
        return 0
    
    elif type(a) == str and type(b)==str:
        return 0
   
    else:
        return a + b
    # if type(a) != float or type(a) != int:
    #     return 0
    # elif type(b) != float or type(b) != int:
    #     return 0
    # else:
    #     return a + b
e = sum(5, 9)
print('sum =', e)

def foo(a):
    print('a:', a)
    a.append('111111111')
    a.append('222')

foo(l)

print('list', l)

def foo1(a):
    a = 333

foo1(b)
print(b)
 
f = {
    'a': 100,
    'b': 200,
    'c': 250,
}

print(type(f))

print(f)