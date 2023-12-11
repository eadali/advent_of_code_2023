import numpy as np


def read_file(path):
    file = open(path, 'r')
    lines = file.readlines()
    removd = []
    for line in lines:
        removd.append(line[:-1])
    return removd


def convert_numpy(lines):
    splitted = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        splitted.append(row)
    return np.array(splitted)


def is_symbol(char):
    cond1 = not char.isdigit()
    cond2 = not (char == '.')
    return cond1 and cond2


def lim_array(i, j, array):
    _i = max(0, min(array.shape[0]-1, i))
    _j = max(0, min(array.shape[1]-1, j))
    return _i, _j


def check_around(array, i, j):
    _i, _j = lim_array(i-1, j-1, array)
    cond1 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i-1, j, array)
    cond2 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i-1, j+1, array)
    cond3 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i, j-1, array)
    cond4 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i, j+1, array)
    cond5 = is_symbol(array[_i, _j])
    # print('--', cond5)

    _i, _j = lim_array(i+1, j-1, array)
    cond6 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i+1, j, array)
    cond7 = is_symbol(array[_i, _j])

    _i, _j = lim_array(i+1, j+1, array)
    cond8 = is_symbol(array[_i, _j])

    return cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8


lines = read_file('input.txt')
array = convert_numpy(lines)

start = False
end = False
valid = False
sum = 0
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        if array[i, j].isdigit():
            if not start:
                start = True
                valid = False
                number = ''
            number = number + array[i, j]
            valid = (valid or check_around(array, i, j))

        else:
            if start:
                print(number, valid)
                if valid:
                    sum = sum + int(number)
                start = False
print(sum)