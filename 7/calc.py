import numpy as np

file = open('example.txt', 'r')
lines = file.readlines()



def compare(hand1, hand2):
    for index in range(len(hand1)):
        if hand1[index] > hand2[index]:
            return 0
        if hand1[index] < hand2[index]:
            return 1



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
bets = np.zeros((len(lines), 1))
for index, line in enumerate(lines):
    first, second = line.split(' ')
    hand = string_to_number(first)
    value = calc_value(hand)
    bet = int(second)
    values[index, 0] = value
    values[index, 1:] = hand
    bets[index] = bet

print(values)
# print(bets)



