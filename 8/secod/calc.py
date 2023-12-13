def get_start(map_):
    keys = []
    for key in map_.keys():
        if key.endswith('A'):
            keys.append(key)
    return keys

def multi(map_, keys, comm):
    new_keys = []
    for key in keys:
        new_keys.append(map_[key][comm])
    return new_keys

def multi_check(keys):
    cond = 0
    for key in keys:
        if key.endswith('Z'):
            cond = cond + 1
            # print('yep')
            # input()
        else:
            cond = 0

    if cond >= 3:
        print(cond * cond * str(cond))

    if cond == 6:
        return True
    return False


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


start_keys = get_start(mapp)
print(start_keys)




i = 0
j = 0

while True:
    if commands[i] == 'R':
        comm_i = 1
    else:
        comm_i = 0
    
    start_keys = multi(mapp, start_keys, comm_i) 
    
    i = i + 1
    j = j + 1
    if multi_check(start_keys):
        break

    if i >= len(commands):
        i = 0

print(j)

