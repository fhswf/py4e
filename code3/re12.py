# Finde Zeilen, die mit 'Details: rev=' beginnen, gefolgt von einer Zahl
# mit einer oder mehr Ziffern und Dezimalpunkten. Diese Zahl ist der Match
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)
