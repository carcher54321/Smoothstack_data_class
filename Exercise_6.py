from random import sample, randint

allNames = ['Frodo', 'Sam', 'Pippin', 'Merry', 'Aragorn', 'Legolas', 'Gimli', 'Gandalf', 'Boromir']


def threeIsACrowd_1(people):
    numPpl = len(people)
    if numPpl > 3:
        print('The room is crowded')


def threeIsACrowd_2(people):
    numPpl = len(people)
    if numPpl > 3:
        print('The room is crowded')
    else:
        print('The room is not very crowded')


def threeIsACrowd_3(people):
    numPpl = len(people)
    if numPpl > 5:
        print('There is a mob in the room')
    elif numPpl > 3:
        print('The room is crowded')
    elif numPpl > 0:
        print('The room is not very crowded')
    else:
        print('The room is empty')


names = sample(allNames, 4)
# over 3, crowded
threeIsACrowd_1(names)
names.pop(0)
names.pop(-1)
# under 3, no output
threeIsACrowd_1(names)
# under 3, not crowded
threeIsACrowd_2(names)

# over 5 names, there is a mob
names = sample(allNames, 7)
threeIsACrowd_3(names)

# 5 random selections
for i in range(5):
    threeIsACrowd_3(sample(allNames, randint(0, 9)))

"""
OUTPUT:
The room is crowded
The room is not very crowded
There is a mob in the room
The room is crowded
There is a mob in the room
There is a mob in the room
The room is crowded
There is a mob in the room
"""
