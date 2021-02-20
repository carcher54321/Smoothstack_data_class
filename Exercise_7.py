from random import randint
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included). Go to the editor
def getNums():
    nums = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)
    print(','.join([str(n) for n in nums]))


getNums()


# Write a Python program to convert temperatures to and from celsius, fahrenheit.
def fahrenheit_to_celsius(f):
    return (f - 32) * (9/5)


def celsius_to_fahrenheit(c):
    return (c * (9/5)) + 32


print(f'60C = {celsius_to_fahrenheit(60)}')
print(f'45F = {fahrenheit_to_celsius(45)}')


def guess_1_9():
    num = randint(1, 10)
    guess = None
    while guess != num:
        if guess:
            print('Incorrect')
        guess = int(input('Guess a number between 1 and 9: '))
    else:
        print('Correct!')


guess_1_9()


# 4.Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
def make_star_pattern(pattern):
    for n in pattern:
        print(' '.join(['*' for _ in range(n)]))


make_star_pattern([1, 2, 3, 4, 5, 4, 3, 2, 1])


# Write a Python program that accepts a word from the user and reverse it.
def rev_string():
    s = input('Enter a string to reverse')
    print(s[::-1])


rev_string()


# Write a Python program to count the number of even and odd numbers from a series of
# numbers.
def count_evens_and_odds(it):
    evens = len([x for x in it if x % 2 == 0])
    odds = len([x for x in it if x % 2 != 0])
    print(f'Number of even numbers: {evens}')
    print(f'Number of odd numbers: {odds}')


count_evens_and_odds((1, 2, 3, 4, 5, 6, 7, 8, 9))


# Write a Python program that prints each item and its corresponding type from the following list.
def printTypes(lst):
    for item in lst:
        print(f'{item}: {type(item)}')


printTypes([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}])


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
def print_non_3s(it):
    for x in it:
        if x % 3 == 0 and x != 0:
            continue
        print(x, end=' ')
    print('')


print_non_3s(range(7))

"""
OUTPUT:
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
60C = 140.0
45F = 23.400000000000002
Guess a number between 1 and 9: 1
Incorrect
Guess a number between 1 and 9: 2
Incorrect
Guess a number between 1 and 9: 3
Correct!
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Enter a string to reverseImaStringgnirtSamI
ImaStringgnirtSamI
Number of even numbers: 4
Number of odd numbers: 5
1452: <class 'int'>
11.23: <class 'float'>
(1+2j): <class 'complex'>
True: <class 'bool'>
w3resource: <class 'str'>
(0, -1): <class 'tuple'>
[5, 12]: <class 'list'>
{'class': 'V', 'section': 'A'}: <class 'dict'>
0 1 2 4 5 

Process finished with exit code 0
"""
