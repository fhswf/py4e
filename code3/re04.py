# Finde Zeilen, die mit 'From' beginnen
# und ein at-Zeichen beinhalten
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
