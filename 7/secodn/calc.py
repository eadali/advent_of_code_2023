import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()


# Assign J to 1
# loop J = 1...max to maximize value





def calc_value(hand):
    max_val = 0
    for i in range(1, 15):
        hand_ = hand.copy()
        hand_[hand_ == 1] = i
        _, counts = np.unique(hand_, return_counts=True)
        if 5 in counts:
            max_val = max(max_val, 10)

        if 4 in counts:
            max_val = max(max_val, 9)

        if 3 in counts:
            if 2 in counts:
                max_val = max(max_val, 8)
            else:
                max_val = max(max_val, 7)

        if np.count_nonzero(counts == 2) == 2:
            max_val = max(max_val, 6)

        if np.count_nonzero(counts == 2) == 1:
            max_val = max(max_val, 5)

        max_val = max(max_val, 4)
        print(i, max_val)
    # print('--------------')
    return max_val


def string_to_number(line):
    hand = []
    for char in line:
        if char == 'T':
            hand.append(10)
        elif char == 'J':
            hand.append(1)
        elif char == 'Q':
            hand.append(12)
        elif char == 'K':
            hand.append(13)
        elif char == 'A':
            hand.append(14)
        else:
            hand.append(int(char))
    return np.array(hand)


values = np.zeros((len(lines), 6))
bets = np.zeros((len(lines)))
for index, line in enumerate(lines):
    first, second = line.split(' ')
    hand = string_to_number(first)
    print(hand)
    value = calc_value(hand)
    bet = int(second)
    values[index, 0] = value
    values[index, 1:] = hand
    bets[index] = bet

values_tr = np.transpose(values)
print(values)
# print(values_tr)


sortedd = np.lexsort(values_tr[::-1, :])
ordered_bets = bets[sortedd]
total = 0
for i in range(len(ordered_bets)):
    total = total + (i+1) * ordered_bets[i]

print(total)

# print(values)
# print(sortedd)
# print(bets)
