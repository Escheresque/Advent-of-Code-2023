
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D10-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

# First we need to find the starting position:
for y in range(0, len(Data)):
    for x in range(0, len(Data[y])):
        if Data[y][x] == "S":
            Start = [y,x]

def NextStep(CurrPos, PrePos):
    N = [CurrPos[0] - 1, CurrPos[1]]
    E = [CurrPos[0], CurrPos[1] + 1]
    S = [CurrPos[0]+ 1, CurrPos[1]]
    W = [CurrPos[0], CurrPos[1] - 1]
    CurrPipe = Data[CurrPos[0]][CurrPos[1]]

    if CurrPipe == "|": 
        if PrePos == S: NextStep = N
        if PrePos == N: NextStep = S

    if CurrPipe == "-":
        if PrePos == E: NextStep = W
        if PrePos == W: NextStep = E

    if CurrPipe == "L":
        if PrePos == N: NextStep = E
        if PrePos == E: NextStep = N

    if CurrPipe == "J":
        if PrePos == N: NextStep = W
        if PrePos == W: NextStep = N

    if CurrPipe == "7":
        if PrePos == S: NextStep = W
        if PrePos == W: NextStep = S

    if CurrPipe == "F":
        if PrePos == S: NextStep = E
        if PrePos == E: NextStep = S

    return [NextStep, CurrPos]

CP = [Start[0] + 1, Start[1]]
PP = Start
d = 1

# Since we will need it in Part 2, we add the coordinates of the MainPipe to a list
MainPipe = [Start]
while Data[CP[0]][CP[1]] != "S":
    MainPipe.append(CP)
    Temp = NextStep(CP, PP)
    CP = Temp[0]
    PP = Temp[1]
    d += 1

D10P1Sol = d * 0.5

# --- Part 2 -----------------------------------------------------------------------------

nData = []

for i, line in enumerate(Data):
    nData.append(list(line))

for y in range(0, len(nData)):
    for x in range(0, len(nData[y])):
        if not([y,x] in MainPipe): nData[y][x] = "x"

# The idea to find if a point is inside or outside is too look in each direction and see if it passes the pipe. 
# Mathematically, if in every direction (in this case there are only 4) we only pass the pipe an odd amount of times, we are inside
#  
miny = 140
maxy = 0
minx = 140
maxx = 0

for pipe in MainPipe:
    miny = min(miny, pipe[0])
    maxy = max(maxy, pipe[0])
    minx = min(minx, pipe[1])
    maxx = max(maxx, pipe[1])

def Shoot(CurrPos):
    currY = CurrPos[0]
    insideElements = 0

    for i in range(minx, maxx + 1):
        ncounter = 0
        scounter = 0
        wcounter = 0
        ecounter = 0

        if nData[currY][i] == "x":
            # Going North
            ncounter = 0
            for k in range(currY - 1, miny-1, -1):
                if nData[k][i] == "-":
                    ncounter += 1
                elif nData[k][i] == "L" or nData[k][i] == "7":
                    ncounter += 0.5
                elif nData[k][i] == "J" or nData[k][i] == "F":
                    ncounter -= 0.5

            # Going South
            scounter = 0
            for k in range(currY + 1, maxy + 1):
                if nData[k][i] == "-":
                    scounter += 1
                elif nData[k][i] == "L" or nData[k][i] == "7":
                    scounter += 0.5
                elif nData[k][i] == "J" or nData[k][i] == "F":
                    scounter -= 0.5

            # Going East
            ecounter = 0
            for k in range(i+1, maxx + 1):
                if nData[currY][k] == "|":
                    ecounter += 1
                elif nData[currY][k] == "L" or nData[currY][k] == "7":
                    ecounter += 0.5
                elif nData[currY][k] == "J" or nData[currY][k] == "F":
                    ecounter -= 0.5

            # Going West
            wcounter = 0
            for k in range(i-1, minx - 1, -1):
                if nData[currY][k] == "|":
                    wcounter += 1
                elif nData[currY][k] == "L" or nData[currY][k] == "7":
                    wcounter += 0.5
                elif nData[currY][k] == "J" or nData[currY][k] == "F":
                    wcounter -= 0.5

        if ncounter % 2 != 0 and scounter % 2 != 0 and wcounter % 2 != 0 and ecounter % 2 != 0:
            insideElements += 1

    return insideElements

D10P2Sol = 0
for y in range(miny, maxy + 1):
    D10P2Sol += Shoot([y, minx])

print("Solution Day 10 P1:", D10P1Sol)
print("Solution Day 10 P2:", D10P2Sol)
