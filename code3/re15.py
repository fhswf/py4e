# Finde Zeilen die das Wort 'New Revision: ' enthalten, gefolg von einer
# Zahl. Überführe diese Zahl in eine Fliesskommazahl und haenge sie an
# die Liste nums an. Gib die Laenge und den Mittelwert von nums aus.
import re
fname = input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
print(len(nums))
print(int(sum(nums)/len(nums)))
