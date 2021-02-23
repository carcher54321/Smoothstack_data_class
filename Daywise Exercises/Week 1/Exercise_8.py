# 1.Create a function func() which prints a text ‘Hello World’
def say_hello():
    print('Hello World')


say_hello()


# 2.Create a function which func1(name) which takes a value name and prints the output “Hi My name is
# Google’
def func1(name):
    print(f'Hi, my name is {name}!')


func1('Google')


# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when
# z is false it should return y . func3(‘hello’goodbye’,false)
def func3(x, y, z):
    if z:
        return x
    else:
        return y


print(func3('hello', 'goodbye', False))


# 4.define a function func4(x,y) which returns the product of both the values.
def func4(x, y):
    return x * y


print(func4(5, 4))


# 5.define a function called as is_even that takes one argument , which returns true when even values is
# passed and false if it is not.
def is_even(n):
    return n % 2 == 0


print(is_even(3))


# 6.define a function that takes two arguments ,and returns true if the first value is greater than the
# second value and returns false if it is less than or equal to the second.
def func5(x, y):
    return x > y


print(func5(5, 4))


# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5, 6, 7))


# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the
# arguments that are even.
def get_evens(*args):
    return [x for x in args if is_even(x)]


print(get_evens(*range(20)))


# 9.Define a function that takes a string and returns a matching string where every even letter is
# uppercase and every odd letter is lowercase
def camelize(s):
    index = 0
    chrs = []
    for ch in s:
        if is_even(index):
            chrs.append(ch.upper())
        else:
            chrs.append(ch.lower())
        index += 1
    return ''.join(chrs)


print(camelize('HAPPY birthday'))


# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns
# greater if one or both or odd.
def func5(x, y):
    if is_even(x) and is_even(y):
        return 'lesser'
    return 'greater'


print(func5(6, 8))


# 11.Write a function which takes two-strings and returns true if both the strings start with the same
# letter.
def func6(s1, s2):
    return s1[0].lower() == s2[0].lower()


print(func6('happy', 'holidays'))


# 12.Given a value,return a value which is twice as far as other side of 7
def func7(n):
    return ((n - 7) * -2) + 7


print(func7(10))


# 13.A function that capitalizes first and fourth character of a word in a string.
def func8(s):
    return s[0].upper() + s[1:3] + s[3].upper() + s[4:]


print(func8('happy'))

"""
OUTPUT:
Hello World
Hi, my name is Google!
goodbye
20
False
True
28
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
HaPpY BiRtHdAy
lesser
True
1
HapPy

Process finished with exit code 0
"""
