import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()


# Assign J to 1
# calc value with J as joker. but always -0.5 from original


def calc_value(hand):
    _, counts = np.unique(hand, return_counts=True)
    if 5 in counts:
        return 10

    if 4 in counts:
        return 9

    if 3 in counts:
        if 2 in counts:
            return 8
        else:
            return 7

    if np.count_nonzero(counts == 2) == 2:
        return 6

    if np.count_nonzero(counts == 2) == 1:
        return 5

    return 4


def string_to_number(line):
    hand = []
    for char in line:
        if char == 'T':
            hand.append(10)
        elif char == 'J':
            hand.append(11)
        elif char == 'Q':
            hand.append(12)
        elif char == 'K':
            hand.append(13)
        elif char == 'A':
            hand.append(14)
        else:
            hand.append(int(char))
    return hand


values = np.zeros((len(lines), 6))
bets = np.zeros((len(lines)))
for index, line in enumerate(lines):
    first, second = line.split(' ')
    hand = string_to_number(first)
    value = calc_value(hand)
    bet = int(second)
    values[index, 0] = value
    values[index, 1:] = hand
    bets[index] = bet

values_tr = np.transpose(values)
print(values)
print(values_tr)


sortedd = np.lexsort(values_tr[::-1, :])
ordered_bets = bets[sortedd]
total = 0
for i in range(len(ordered_bets)):
    total = total + (i+1) * ordered_bets[i]

print(total)

# print(values)
# print(sortedd)
# print(bets)
