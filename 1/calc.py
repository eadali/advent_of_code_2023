values = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def convert(val):
    if len(val) == 1:
        return int(val)
    else:
        if val == 'one':
            return 1
        elif val == 'two':
            return 2
        elif val == 'three':
            return 3
        elif val == 'four':
            return 4
        elif val == 'five':
            return 5
        elif val == 'six':
            return 6
        elif val == 'seven':
            return 7
        elif val == 'eight':
            return 8
        elif val == 'nine':
            return 9


def find_index(line):
    minn = 10000
    for val in values:
        index = line.find(val)
        if (index < minn) and (index > -0.5):
            first = val
            minn = index

    minn = -1
    for val in values:
        index = line.rfind(val)
        if index > minn:
            second = val
            minn = index
    
    return convert(first), convert(second)

    print(first, second)


# def hh(stt, line):
#     index = line.find(stt)
#     if index >=0:

# def replace_num(line):
#     line = line.replace('one', '1')
#     line = line.replace('two', '2')
#     line = line.replace('three', '3')
#     line = line.replace('four', '4')
#     line = line.replace('five', '5')
#     line = line.replace('six', '6')
#     line = line.replace('seven', '7')
#     line = line.replace('eight', '8')
#     line = line.replace('nine', '9')
#     return line


file = open('input.txt', 'r')
lines = file.readlines()
sum = 0
for line in lines:
    a,b = find_index(line)

    aa = a*10 + b
    sum = sum + aa
print(sum)


# print(line)
    # line = replace_num(line)
    # print(line)
    # for ch in line:
    #     if ch.isdigit():
    #         first = ch
    #         break
    # for ch in line[::-1]:
    #     if ch.isdigit():
    #         second = ch
    #         break
    # print(first)
    # print(second)
