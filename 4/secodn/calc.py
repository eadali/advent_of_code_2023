import numpy as np


file = open('input.txt', 'r')
lines = file.readlines()

array = np.zeros((len(lines), 2), dtype=np.uint32)
for index, line in enumerate(lines):
    card, numbers = line.split(': ')
    winners, mines = numbers.split(' | ')
    winner_nums = []
    for num in winners.split(' '):
        if num != '':
            winner_nums.append(int(num))

    mine_nums = []
    for num in mines.split(' '):
        if num != '':
            mine_nums.append(int(num))
    
    total = 0
    for win in winner_nums:
        for mine in mine_nums:
            if win == mine:
                total = total + 1
    
    array[index, 0] = total
    array[index, 1] = 1
    


for index in range(array.shape[0]):
    next_card_num = array[index, 0]
    start_lim = min(array.shape[0]-1, index + 1)
    end_lim = int(min(array.shape[0]-1, index + next_card_num+1))

    array[start_lim:end_lim, 1] = array[start_lim:end_lim,1] + array[index, 1]



# summ = 0
# for index in range(array.shape[0]):
#     if 
#     if array[index, 0] == 1:
#         summ = summ + 1
#     elif array[index, 0] > 1:
#         summ = summ + 2**(array[index, 0]-1)
# print(summ)



print(array)
# print(array.sum(axis=0))
print(array.sum(axis=0)[1])