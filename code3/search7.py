fname = input('Gib eine Datei an: ')
try:
    fhand = open(fname)
except:
    print(f'Datei {fname} konnte nicht geoeffnet werden')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print(f'Es gibt {count} Betreffzeilen in {fname}')
