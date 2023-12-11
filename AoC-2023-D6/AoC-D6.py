
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D6-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

D1 = []
for line in Data:
    D1.append(line.split())

D2 = [['Time:', '38947970'],['Distance:', '241154910741001']]

def FindSol(D3):
    Possibilities = []
    for r in range(1, len(D3[0])):
        t = int(D3[0][1])
        d = int(D3[1][1])
        WinningPressTime = []
        for i in range(0, t):
            if (t-i)*i > d:
                WinningPressTime.append(i)

        Possibilities.append(WinningPressTime)
    return Possibilities

P1 = FindSol(D1)
P2 = FindSol(D2)

SolP1 = 1
for p in P1:
    SolP1 = SolP1 * len(p)

SolP2 = len(P2[0])

print("Solution Part 1: ", SolP1)
print("Solution Part 2: ", SolP2)




