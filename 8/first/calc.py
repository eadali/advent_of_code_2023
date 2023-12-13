lines = open('input.txt', 'r').readlines()

mapp = {}

commands = lines[0].replace('\n', '')

for index in range(2, len(lines)):
    key, rest = lines[index].split('=')
    key = key.replace(' ', '')
    rest = rest.replace('(', '').replace(')', '').replace(' ', '')
    rest = rest.replace('\n', '')
    val1, val2 = rest.split(',')

    mapp[key] = (val1, val2)

i = 0
j = 0
key = 'AAA'
while True:
    comm = commands[i]
    if comm == 'R':
        key = mapp[key][1]
    else:
        key = mapp[key][0]
    
    i = i + 1
    j = j + 1
    if key == 'ZZZ':
        break
    if i >= len(commands):
        i = 0

print(j)

