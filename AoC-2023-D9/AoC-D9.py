
Data = []
ataD = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D9-Data.txt") as file:
    for line in file:
        CurrLine = [eval(i) for i in line.rstrip().split()]
        Data.append(CurrLine)
        ataD.append(CurrLine[::-1])

def nextList(L1):
    NL = []
    for i in range(0, len(L1) - 1):
        NL.append(L1[i+1] - L1[i])
    return NL

def BuildPyramid(I1):
    Archive = [I1]
    AllZeroes = False
    while AllZeroes == False:
        I1 = nextList(I1)
        Archive.append(I1)
        if all(v == 0 for v in I1): AllZeroes = True
    return Archive

def GoBackUp(Pyramid):
    Pyramid[len(Pyramid)-1].append(0)
    for i in range(len(Pyramid) - 2, -1, -1):
        Pyramid[i].append(Pyramid[i][-1] + Pyramid[i+1][-1])
    return Pyramid

# Start Code
    
AllPyramids = []
for line in Data:
    Pyra = BuildPyramid(line)
    AllPyramids.append(Pyra)

P1Solution = 0
for pyra in AllPyramids:
    newPyra = GoBackUp(pyra)
    P1Solution += newPyra[0][-1]

sdimaryPllA = []
for enil in ataD:
    aryP = BuildPyramid(enil)
    sdimaryPllA.append(aryP)

noituloS2P = 0
for aryp in sdimaryPllA:
    aryPwen = GoBackUp(aryp)
    noituloS2P += aryPwen[0][-1]

print("Day 9 P1 Solution: ", P1Solution)
print("Day 9 P2 Solution: ", noituloS2P)





