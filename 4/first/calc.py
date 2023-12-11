file = open('input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
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
                if total == 0:
                    total = 1
                else:
                    total = total * 2
    sum = sum + total
    
print(sum)