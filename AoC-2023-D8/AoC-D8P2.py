import math

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-2023-D8\AoC-D8.txt") as file:
    for line in file:
        Data.append(line.rstrip())

LR = Data[0]
PosList = []
LList = []
RList = []

for i in range(0, len(Data[2:])):
    PosList.append(Data[2:][i][0:3])
    LList.append(Data[2:][i][7:10])
    RList.append(Data[2:][i][12:15])

AStarts = []
for coord in PosList:
    if coord[2] == "A":
        AStarts.append(coord)

Arrived = False
NX1 = ["AAA", "SLH", "CVN"]
NX2 = ["MGA", "PLT", "NCP"]
NX3 = ["DGA", "FTD", "RGR"]
NX4 = ["TLA", "QXP", "MKM"]
NX5 = ["RDA", "BVG", "DJM"]
NX6 = ["DPA", "MDS", "SHG"]

def NextStep(d, ThreePostitions):
    
    CurrPos = ThreePostitions[0]
    LNext = ThreePostitions[1]
    RNext = ThreePostitions[2]

    if d == "L":
        CurrPos = PosList[PosList.index(LNext)]
        LNext = LList[PosList.index(CurrPos)]
        RNext = RList[PosList.index(CurrPos)]
    elif d == "R":
        CurrPos = PosList[PosList.index(RNext)]
        LNext = LList[PosList.index(CurrPos)]
        RNext = RList[PosList.index(CurrPos)]

    return [CurrPos, LNext, RNext]

CycleLengths = [0, 0, 0, 0, 0, 0]
C1 = False
C2 = False
C3 = False
C4 = False
C5 = False
C6 = False

Steps = 0
while Arrived == False:
    for d in LR: 

        NX1 = NextStep(d, NX1)
        NX2 = NextStep(d, NX2)
        NX3 = NextStep(d, NX3)
        NX4 = NextStep(d, NX4)
        NX5 = NextStep(d, NX5)
        NX6 = NextStep(d, NX6)
        Steps += 1

        if NX1[0][2] == "Z" and C1 == False:
            CycleLengths[0] = Steps
            C1 = True

        if NX2[0][2] == "Z" and C2 == False:
            CycleLengths[1] = Steps
            C2 = True

        if NX3[0][2] == "Z" and C3 == False:
            CycleLengths[2] = Steps
            C3 = True

        if NX4[0][2] == "Z" and C4 == False:
            CycleLengths[3] = Steps
            C4 = True

        if NX5[0][2] == "Z" and C5 == False:
            CycleLengths[4] = Steps
            C5 = True

        if NX6[0][2] == "Z" and C6 == False:
            CycleLengths[5] = Steps
            C6 = True

        if NX1[0][2] == "Z" and NX2[0][2] == "Z" and NX3[0][2] == "Z" and NX4[0][2] == "Z" and NX5[0][2] == "Z" and NX6[0][2] == "Z":
            Arrived = True
            Solution = Steps
            break

        if C1 and C2 and C3 and C4 and C5 and C6:
            Arrived = True
            break

        if Steps % 100000 == 0:
            print("Already walked ", Steps, " Steps0")

S = CycleLengths
Solution = math.lcm(S[0], S[1], S[2], S[3], S[4], S[5])

print("D8 P2 Solution: ", Solution)



