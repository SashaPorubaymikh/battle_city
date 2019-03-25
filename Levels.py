flevel1 = open('levels/level_1.txt', 'r')
flevel2 = open('levels/level_2.txt', 'r')
level1 = []
level2 = []
def mklv(file, list):
    for line in file:
        list.append(line)
mklv(flevel1, level1)
mklv(flevel2, level2)