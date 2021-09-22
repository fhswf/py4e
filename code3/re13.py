# Finde Zeilen, die mit 'From ' beginnen und dann irgendwann eine Zahl
# genau mit genau zwei Ziffern steht. Vor der zweistellingen Zahl muss ein
# Leerzeichen stehen, danach ein ':'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)
