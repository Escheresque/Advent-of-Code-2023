import numpy as np

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-2023-D11\AoC-D11.txt") as file:
    for line in file:
        DataLine = []
        for l in line.rstrip():
            DataLine.append(l)
        Data.append(DataLine)

OldData = Data

# We just change the empty space with h's and v's to represent empty rows

for col in range(0, len(Data[0])):
    CurrColGalaxy = False
    for row in range(0, len(Data)):
        if Data[row][col] == "#":
            CurrColGalaxy = True
    if CurrColGalaxy == False:
        for row in range(0, len(Data)):
            Data[row][col] = "v"


for row in range(0, len(Data)):
    CurrRowGalaxy = False
    for col in range(0, len(Data[0])):
        if Data[row][col] == "#":
            CurrRowGalaxy = True
    if CurrRowGalaxy == False:
        for col in range(0, len(Data[0])):
            Data[row][col] = "h"
 

# Then we have to check where each universe is located 
UniLocs = []
for row in range(0, len(Data)):
    for col in range(0, len(Data[0])):
        if Data[row][col] == "#":
            UniLocs.append([row, col])

def Walk(s, e, d):
    DDD = Data
    srow = s[0]
    scol = s[1]
    erow = e[0]
    ecol = e[1]
    
    steps = 0

    for hstep in range(min(scol, ecol), max(scol, ecol)):
        if Data[srow][hstep] == "v":
            steps += d
        else:
            steps += 1

    for vstep in range(min(srow, erow), max(srow, erow)):
        if Data[vstep][srow] == "h":
            steps += d
        else:
            steps += 1

    return steps

D11P1Sol = 0
D11P2Sol = 0
for s in range(0, len(UniLocs)-1):
    print(s, "out of", len(UniLocs))
    StartUni = UniLocs[s]
    for e in range(s+1, len(UniLocs)):
        EndUni = UniLocs[e]
        # Here we walk the path
        D11P1Sol += Walk(StartUni, EndUni, 2)
        D11P2Sol += Walk(StartUni, EndUni, 1000000)
      
print("D11 P1 Solution: ", D11P1Sol)
print("D11 P2 Solution: ", D11P2Sol)
