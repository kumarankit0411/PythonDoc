file = open('mods.txt', 'r')

for line in file:
    if line!='\n':
        print(line, end='')
