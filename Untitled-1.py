# Lesson first
print("Hello world!")
print("I am Alex!")
#name = input("Please enter your name: ")
#print("Hi " + name)

x = 3
y = 4
print(x, y)

x,y = y,x
print(x, y)
print(type(x))
print(x ** 3)
print(x % 3)

z = float(x)
print(z)
w = 1.3333
print(int(w))
print(round(w))

flaut_num = 21

entarance_num = (flaut_num - 1) // 20 + 1
floor_num = (flaut_num - 1) % 20 //4 + 1
print(entarance_num)
print(floor_num)

# Lesson second

t = True
f = False

print(t, f)
print(t == f)
print(t != f)

x = 1
print(x > -1 and x < 5)
x = 6
print(x > -1 and x < 5)

print(not f)

print('Bool')
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(10000))
print(bool(''))
print(bool('.'))

print('If')
if True:
    print('Its true')

x = 10
if x > 0:
    print('x more than 0')
elif x < 0:
    print('x less than 0')
else:
    print('x is 0')

y = 4
if y != 0 and y < 5:
    print('y is smaller than 5 but not a zero')

year = 2026
if year % 4 == 0 and year % 100 != 0:
    print('Year is leap')
elif year % 400 == 0:
    print('Year is leap')
else:
    print('Year is not leap')

#Lesson third
my_string = """
Hi
I
am Nomex
"""
print(my_string)

name = 'Alex'
length = len(name)
print(length)

my_str = 'Hello'
print("Hell0" in my_str)
print(my_str.upper())
print(my_str.upper().lower())
print(my_str.replace('Hello', 'Hell0'))
print(my_str.count('l'))

integer = '10q'
if integer.isdigit():
    integer = int(integer)
print(integer.isdigit())
print('10'.isdigit())

age = 17
print(f"Hi my name is {name} and I'm {age} years old")

#message = input('Enter the number: ')
message = '1o'
if message.isdigit():
    message = int(message)
    print(f'{message} is a number')
    print(type(message))
else:
    print(f'{message} is not a number')
    print(type(message))