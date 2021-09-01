# Finde Zeilen die das Wort 'Author:' enthalten, gefolg von beliebigen
# Zeichen, einem at-Zeichen und einem oder mehr (nicht Leer-)Zeichen.
# Die Zeichen nach dem at sind der Match
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)
