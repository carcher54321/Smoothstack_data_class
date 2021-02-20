
def calc_BMI(w, h):
    return w / (h**2)


def categorize(bmi):
    if bmi < 18.5:
        return 'under'
    elif bmi < 25:
        return 'normal'
    elif bmi < 30:
        return 'over'
    else:
        return 'obese'


def get_inputs():
    n = int(input())
    data = []
    for i in range(n):
        inp = input()
        w, h = inp.split()
        data.append((int(w), float(h)))
    for row in data:
        ret = categorize(calc_BMI(*row))
        print(ret, end=' ')
    print()


get_inputs()
"""
OUTPUT:
3
80 1.73
55 1.58
49 1.91
over normal under 

Process finished with exit code 0
"""
