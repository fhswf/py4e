numlist = list()
while (True):
    inp = input('Gib eine Zal ein: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Mittelwert:', average)
