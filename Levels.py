flevel1 = open('levels/level_1', 'r')
flevel2 = open('levels/level_2', 'r')
flevel3 = open('levels/level_3', 'r')
flevel4 = open('levels/level_4', 'r')

level1 = []
level2 = []
level3 = []
level4 = []
def mklv(file, list):
    for line in file:
        list.append(line)
mklv(flevel1, level1)
mklv(flevel2, level2)
mklv(flevel3, level3)
mklv(flevel4, level4)
levels = [level1, level2, level3, level4]