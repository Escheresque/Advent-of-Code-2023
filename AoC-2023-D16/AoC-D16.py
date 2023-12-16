from copy import deepcopy
import pandas
import sys

sys.setrecursionlimit(999999)

Data = []
FirstRow = True
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D16\AoC-D16.txt") as file:
    for line in file:
        templine = line.rstrip()
        temprow = ["x"]

        xRow = ["x", "x"]
        for i in range(0, len(templine)):
            xRow.append("x")

        if FirstRow:
            Data.append(xRow)
            FirstRow = False

        for t in templine:
            if t == "\\":
                temprow.append('b')
            else:
                temprow.append(t)

        temprow.append("x")      
        Data.append(temprow)

Data.append(xRow.copy())

DataVis = deepcopy(Data)

precoord = [1, 0]
currcoord = [1,1]

EnergizedCoords = []
AlreadySeen = []

def NextStep(CurrPos, PrePos):

    row = CurrPos[0]
    col = CurrPos[1]

    DataVis[row][col] = "#"

    if not(CurrPos in EnergizedCoords):
        EnergizedCoords.append(CurrPos)

    if not([CurrPos, PrePos] in AlreadySeen):
        AlreadySeen.append([CurrPos, PrePos])
    else:
        return

    if Data[row][col] == "x":
        return

    N = [row - 1, col]
    E = [row, col + 1]
    S = [row + 1, col]
    W = [row, col - 1]
    CurrMirr = Data[row][col]

    if CurrMirr == ".":
        if PrePos == N: NextStep(S, CurrPos)
        elif PrePos == S: NextStep(N, CurrPos)
        elif PrePos == W: NextStep(E, CurrPos)
        elif PrePos == E: NextStep(W, CurrPos)

    if CurrMirr == "|":
        if PrePos == N: NextStep(S, CurrPos)
        elif PrePos == S: NextStep(N, CurrPos)
        elif PrePos == W or PrePos == E: 
            NextStep(S, CurrPos)
            NextStep(N, CurrPos)

    if CurrMirr == "-":
        if PrePos == N or PrePos == S: 
            NextStep(E, CurrPos)
            NextStep(W, CurrPos)
        elif PrePos == W: NextStep(E, CurrPos)
        elif PrePos == E: NextStep(W, CurrPos)

    if CurrMirr == "/":
        if PrePos == N: NextStep(W, CurrPos)
        elif PrePos == S: NextStep(E, CurrPos)
        elif PrePos == W: NextStep(N, CurrPos)
        elif PrePos == E: NextStep(S, CurrPos)

    if CurrMirr == "b":
        if PrePos == N: NextStep(E, CurrPos)
        elif PrePos == S: NextStep(W, CurrPos)
        elif PrePos == W: NextStep(S, CurrPos)
        elif PrePos == E: NextStep(N, CurrPos)

def killEdges(ener):

    for coord in ener:
        if coord[0] == 0 or coord[0] == len(Data) - 1 or coord[1] == len(Data) - 1 or coord[1] == 0:
            ener.remove(coord)

    return ener

NextStep(currcoord, precoord)

for coord in EnergizedCoords:
    if coord[0] == 0 or coord[0] == len(Data) - 1 or coord[1] == len(Data) - 1 or coord[1] == 0:
        EnergizedCoords.remove(coord)

D16P1Sol = 0 
for row in range(1, len(DataVis) - 1):
    for col in range(1, len(DataVis[0]) - 1):
        if DataVis[row][col] == "#":
            D16P1Sol += 1

maxEnergized = 0

# Left Edge          
for l in range(1, len(Data) - 1):
    precoord = [l, 0]
    newcoord = [l, 1]
    EnergizedCoords = []
    AlreadySeen = []
    NextStep(newcoord, precoord)
    print("Left", l, "out of", len(Data) - 1, " - Result: ", len(killEdges(EnergizedCoords)))
    maxEnergized = max(maxEnergized, len(killEdges(EnergizedCoords)))

         
# Right Edge
for r in range(1, len(Data) - 1):
    precoord = [r, len(Data[0]) - 1]
    newcoord = [r, len(Data[0]) - 2]
    EnergizedCoords = []
    AlreadySeen = []
    NextStep(newcoord, precoord)
    print("Right", r, "out of", len(Data) - 1, " - Result: ", len(killEdges(EnergizedCoords)))
    maxEnergized = max(maxEnergized, len(killEdges(EnergizedCoords)))
            
# Top
for t in range(1, len(Data[0]) - 1):
    precoord = [0, t]
    newcoord = [1, t]
    EnergizedCoords = []
    AlreadySeen = []
    NextStep(newcoord, precoord)
    print("Top", t, "out of", len(Data[0]) - 1, " - Result:", len(killEdges(EnergizedCoords)))
    maxEnergized = max(maxEnergized, len(killEdges(EnergizedCoords)))
            
# Bottom
for b in range(1, len(Data[0]) - 1):
    print("Bot", b, "out of", len(Data[0]) - 1)
    precoord = [len(Data) - 1, b]
    newcoord = [len(Data) - 2, b]
    EnergizedCoords = []
    AlreadySeen = []
    NextStep(newcoord, precoord)
    print("Bot", b, "out of", len(Data[0]) - 1, " - Result:", len(killEdges(EnergizedCoords)))
    maxEnergized = max(maxEnergized, len(killEdges(EnergizedCoords)))

D16P2Sol = maxEnergized

print("D16 P1 Solution: ", D16P1Sol)
print("D16 P2 Solution: ", D16P2Sol)

