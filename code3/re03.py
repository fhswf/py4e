# Finde Zeilen die mit einem 'F' beginnen, gefolgt
# von 2 beliebigen Zeichen, gefolgt von einem 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)
