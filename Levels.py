flevel1 = open('levels/level_1', 'r')
flevel2 = open('levels/level_2', 'r')
flevel3 = open('levels/level_3', 'r')
flevel4 = open('levels/level_4', 'r')
flevel5 = open('levels/level_5', 'r')
flevel6 = open('levels/level_6', 'r')
flevel7 = open('levels/level_7', 'r')

level1 = []
level2 = []
level3 = []
level4 = []
level5 = []
level6 = []
level7 = []
def mklv(file, list):
    for line in file:
        list.append(line)
mklv(flevel1, level1)
mklv(flevel2, level2)
mklv(flevel3, level3)
mklv(flevel4, level4)
mklv(flevel5, level5)
mklv(flevel6, level6)
mklv(flevel7, level7)
levels = [level1, level2, level3, level4, level5, level6, level7]