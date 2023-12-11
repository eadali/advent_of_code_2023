def remove_game(line):
    i = line.find(':')+2
    line = line[i:]
    return line


def custom_split(line):
    # line = line.replace(';', ',')
    return line.split(', ')


def count(list_line):
    red = 0
    green = 0
    blue = 0
    for one in list_line:
        num, val = one.split(' ')
        if val == 'red':
            red = red + int(num)
        if val == 'green':
            green = green + int(num)
        if val == 'blue':
            blue = blue + int(num)
    return red, green, blue


def check_valid(red, green, blue):
    cond1 = red <= 12
    cond2 = green <= 13
    cond3 = blue <= 14
    return cond1 and cond2 and cond3

def remove_end(line):
    return line[:-1]


file = open('input.txt', 'r')
lines = file.readlines()

summ = 0
for index, line in enumerate(lines):
    line = remove_game(line)
    line = remove_end(line)
    good = True
    min_red = 0
    min_green = 0
    min_blue = 0
    for turn in line.split('; '):
        list_line = custom_split(turn)
        red, green, blue = count(list_line)
        if red > min_red:
            min_red = red
        if green > min_green:
            min_green = green
        if blue > min_blue:
            min_blue = blue
    summ = summ + min_red*min_green*min_blue
        
        # if not check_valid(red, green, blue):
            # good = False
            # break
            # print(index + 1, '--', red, green, blue)
        #  break
    # if good:
        # summ = summ + index + 1
print(summ)
