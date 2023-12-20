from heapq import heappush, heappop
from copy import deepcopy
import pandas
import xlsxwriter

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D18\AoC-D18.txt") as file:
    for line in file:
        TempRow = line.rstrip().split(" ")
        TempRow[1] = int(TempRow[1])
        Data.append(TempRow)

UBound = 0
DBound = 0
LBound = 0
RBound = 0

for line in Data:
    if line[0] == "U": UBound += line[1]
    elif line[0] == "D": DBound += line[1]
    elif line[0] == "R": RBound += line[1]
    elif line[0] == "L": LBound += line[1]

OutsideAmt = 0

# Here we create the full grid
print("Creating Grid...")
Map = []
for row in range(0, 1000):
    TempRow = ["."] * 1000
    Map.append(deepcopy(TempRow))
print("Finished creating Grid")

def Shoot(CurrPos):
    currrow = CurrPos[0]
    currcol = CurrPos[1] 
    
    insideElements = 0

    if currrow == 500 and currcol == 600:
        print("Stop")

    ncounter = 0
    scounter = 0
    wcounter = 0
    ecounter = 0

    # Going North
    ncounter = 0
    for k in range(currrow, minrow - 10, -1):
        if Map[k][currcol] == "-":
            ncounter += 1
        elif Map[k][currcol] == "L" or Map[k][currcol] == "7":
            ncounter += 0.5
        elif Map[k][currcol] == "J" or Map[k][currcol] == "F":
            ncounter -= 0.5

    # Going South
    scounter = 0
    for k in range(currrow, maxrow + 10):
        if Map[k][currcol] == "-":
            scounter += 1
        elif Map[k][currcol] == "L" or Map[k][currcol] == "7":
            scounter += 0.5
        elif Map[k][currcol] == "J" or Map[k][currcol] == "F":
            scounter -= 0.5

    # Going East
    ecounter = 0
    for k in range(currcol, maxcol + 10):
        if Map[currrow][k] == "|":
            ecounter += 1
        elif Map[currrow][k] == "L" or Map[currrow][k] == "7":
            ecounter += 0.5
        elif Map[currrow][k] == "J" or Map[currrow][k] == "F":
            ecounter -= 0.5

    # Going West
    wcounter = 0
    for k in range(currcol, mincol - 10, -1):
        if Map[currrow][k] == "|":
            wcounter += 1
        elif Map[currrow][k] == "L" or Map[currrow][k] == "7":
            wcounter += 0.5
        elif Map[currrow][k] == "J" or Map[currrow][k] == "F":
            wcounter -= 0.5

    if ncounter % 2 != 0 and scounter % 2 != 0 and wcounter % 2 != 0 and ecounter % 2 != 0:
        insideElements += 1
        Map[currrow][currcol] = "O"

    return insideElements

# Here we paint a Map in a way that we can also translate it into our D12 Code

def AfterSteps(CurrDir, NextDir, S):

    if CurrDir == "U":

        if NextDir == "L":
            Map[S[0]][S[1]] = "7"
            S[1] -= 1

        elif NextDir == "R":
            Map[S[0]][ S[1]] = "F"
            S[1] += 1

    elif CurrDir == "D":

        if NextDir == "L":
            Map[S[0]][S[1]] = "J"
            S[1] -= 1 

        elif NextDir == "R":
            Map[S[0]][ S[1]] = "L"
            S[1] += 1

    elif CurrDir == "L":

        if NextDir == "D":
            Map[S[0]][S[1]] = "F"
            S[0] += 1

        elif NextDir == "U":
            Map[S[0]][ S[1]] = "L"
            S[0] -= 1

    elif CurrDir == "R":

        if NextDir == "D":
            Map[S[0]][S[1]] = "7"
            S[0] += 1

        elif NextDir == "U":
            Map[S[0]][ S[1]] = "J"
            S[0] -= 1

    return S


S = [500, 500]
Map[S[0]][S[1]+1] = "7"

for i, line in enumerate(Data):

    if i % 10 == 0 and i > 0:
        print(i, "/lol", len(Data), " - ", line)

    if line[1] - 1 == 0:
        Map[S[0]][S[1]] = "#"

    for t in range(0, line[1] - 1):
        if line[0] == "U":
        
            Map[S[0]][S[1]] = "|"
            S = [S[0] - 1, S[1]]

        elif line[0] == "D":

            Map[S[0]][S[1]] = "|"
            S = [S[0] + 1, S[1]]

        elif line[0] == "L":

            Map[S[0]][S[1]] = "-"
            S = [S[0], S[1] - 1]

        elif line[0] == "R":

            Map[S[0]][S[1]] = "-"
            S = [S[0], S[1] + 1]

    if i+1 < len(Data):
        S = AfterSteps(line[0], Data[i+1][0], S)

minrow = 99999999
maxrow = 0
mincol = 99999999
maxcol = 0

for row, line in enumerate(Map):
    if row % 100 == 0 and row > 0:
        print("Searching Dots in Row:", row, "/", len(Map))
    for col, sym in enumerate(Map[row]):
        if Map[row][col] != ".":
            minrow = min(row, minrow)
            maxrow = max(row, maxrow)
            mincol = min(col, mincol)
            maxcol = max(col, maxcol)


InsideAmt = 0
for row in range(minrow - 50, maxrow + 50):
    if row % 50 == 0:
       print("Shooting Row:", minrow + row, "out of", minrow + maxrow + 1)

    for col in range(mincol - 50, maxcol + 50):
        sym = Map[row][col]
        if sym == "J" or sym == "F" or sym == "7" or sym == "L" or sym == "|" or sym == "-":
            OutsideAmt += 1
        else:
            InsideAmt += Shoot([row, col])

OutsideAmt2 = 0
for line in Data:
    OutsideAmt2 += line[1]

with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D18\Visualization.txt", 'w') as f:
    for line in Map:
        for letter in line:
            if letter == "---":
                f.write("-")
            else:
                f.write(letter)
        f.write("\n")

print("Outside:", OutsideAmt)
print("Inside:", InsideAmt)
print("D18 P1 Solution:", InsideAmt + OutsideAmt)
        

