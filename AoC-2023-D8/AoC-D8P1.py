
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

Arrived = False
CurrPosition = "AAA"
LNext = "SLH"
RNext = "CVN"
NextCoords = ["AAA", "SLH", "CVN"]

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

Steps = 0
while Arrived == False:
    for d in LR: 

        NextCoords = NextStep(d, NextCoords)
        Steps += 1

        if NextCoords[0] == 'ZZZ':
            Arrived = True
            Solution = Steps
            break

        if Arrived == True:
            break

print("D8 P1 Solution: ", Solution)



