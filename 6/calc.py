import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()

line1 = lines[0].split(':')[1].lstrip().rstrip()
times = [int(i) for i in line1.split('     ')]
times = np.array(times)


line2 = lines[1].split(':')[1].lstrip().rstrip()
distances = [int(i) for i in line2.split('  ')]
distances = np.array(distances)

print(times)
print(distances)


aa = 1
for index in range(times.shape[0]):
    total = 0
    for test in range(times[index]):
        dist = test * (times[index] - test)
        if dist > distances[index]:
            total = total + 1
    aa = aa * total
print(aa)


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = -1
b = 49877895
c = -356137815021882
print(b)

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
