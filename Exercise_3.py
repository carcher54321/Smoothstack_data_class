# Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a
# variable name to the string.
print('Hello World'[8])

# String slicing to grab the word ‘ink’ from the word ‘thinker’
# S=’hello’,what is the output of h[1]
print('thinker'[2:5])
print('hello'[1])  # 'e'

# S=’Sammy’ what is the output of s[2:]”
print('Sammy'[2:])  # 'mmy'

# With a single set function can you turn the word ‘Mississippi’ to distinct character word.
print(set('Mississippi'))


def replaceAll(s, stopChars):
    for char in stopChars:
        s = s.replace(char, '')
    return s


# determine palindromes
def getPalindromes():
    numStrs = int(input())
    phrases = []
    for i in range(numStrs):
        phrases.append(input())
    answers = []
    for phrase in phrases:
        squished = replaceAll(phrase, ' ,!.?\'').lower()
        if squished == squished[::-1]:
            answers.append('Y')
        else:
            answers.append('N')
    print(' '.join(answers))


getPalindromes()
"""
OUTPUT:
r
ink
e
mmy
{'i', 's', 'M', 'p'}
3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos
N Y Y
"""
