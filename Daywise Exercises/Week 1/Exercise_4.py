# Create a list with one number, one word and one float value. Display the output of the list.
lst = ['hello', 4.2]
print(lst)

# I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.
lst = [1, 1, [1, 2]]
print(lst[2][1])

# lst=['a', 'b', 'c'] What is the result of lst[1:]?
# lst[1:] = ['b', 'c']
lst = ['a', 'b', 'c']
print(lst[1:])

# Create a dictionary with weekdays an keys and week index numbers as values.do assign
# dictionary to a variable
weekdayIndices = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 7}

# D={‘k1’:[1,2,3]} what is the output of d[k1][1]
# d['k1'][1] = 2
d = {'k1': [1, 2, 3]}
print(d['k1'][1])

# With a single set function can you turn the word ‘Mississippi’ to distinct character word.
s = set('Mississippi')
print(s)
# getting it back to a nice string is more than one line

# Can you add an element ‘X’ to the above created set
s.add('X')
print(s)

# Output of set([1,1,2,3])
# {1, 2, 3}
print(set([1, 1, 2, 3]))


# find all numbers which are multiples of 7 but not of 5 between 2000 and 3200 inclusive
def getNums():
    nums = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)
    print(','.join([str(n) for n in nums]))


getNums()


def getFactorial(num):
    if num == 0:
        return 1
    return num * getFactorial(num - 1)


inp = int(input('Enter a number to get the factorial: '))
print(getFactorial(inp))


def getSquares(num):
    d = {}
    for i in range(1, num + 1):
        d[i] = i * i
    return d


inp = int(input('Enter a number to get squares: '))
print(getSquares(inp))


def splitNums():
    values = input('Enter comma-separated numbers: ')
    l = [int(x) for x in values.split(',')]
    t = tuple(l)
    print(l)
    print(t)


splitNums()


class InOutString:

    def __init__(self):
        self._s = ''

    @staticmethod
    def test():
        Obj = InOutString()
        Obj.getString()
        Obj.printString()

    def getString(self):
        self._s = input('Enter a new string: ')

    def printString(self):
        print(self._s.upper())


InOutString.test()
"""
OUTPUT:
['hello', 4.2]
2
['b', 'c']
2
{'p', 'M', 'i', 's'}
{'X', 'M', 'i', 'p', 's'}
{1, 2, 3}
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199
Enter a number to get the factorial: 8
40320
Enter a number to get squares: 8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Enter comma-separated numbers: 4,52,23,49,91,74,28
[4, 52, 23, 49, 91, 74, 28]
(4, 52, 23, 49, 91, 74, 28)
Enter a new string: Wheeeeee I'm a string
WHEEEEEE I'M A STRING
"""
