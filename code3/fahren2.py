inp = input('Gib die Temperatur in Fahrenheit ein: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Bitte gib eine Zahl ein!')
