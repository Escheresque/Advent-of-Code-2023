
Data1 = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D18\AoC-D18.txt") as file:
    for line in file:
        TempRow = line.rstrip().split(" ")
        TempRow[1] = int(TempRow[1])
        Data1.append(TempRow)

Data2 = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D18\AoC-D18.txt") as file:
    for line in file:
        TempRow = []
        Hexa = line.split("#")[1]

        if Hexa[5] == "0":
            TempRow.append("R")
        elif Hexa[5] == "1":
            TempRow.append("D")
        elif Hexa[5] == "2":
            TempRow.append("L")
        elif Hexa[5] == "3":
            TempRow.append("U")

        TempRow.append(int('0x' + Hexa[0:5], base = 16))
        Data2.append(TempRow)

def NextCorner(Position,Direction,Length):
    return (Position[0]+Length*Direction[0], Position[1]+Length*Direction[1])

# PART 1 
        
Corners = [(0,0)]
Directions = {'R':(1,0), 'L':(-1,0), 'D':(0,-1), 'U':(0,1)}
NewPosition = (0,0)

# We will use the Satz of Pick
#
# A = I + R/2 - 1
#
# With A = Area of the Polygon, I = Points Inside and R = Outside Length

# With the Gauß'sche Trapezformel (Shoelace Formula) we can calculate the Area of the Polygon:
# Being at a Corner (row_i, col_i), we attach to the Edge (row_i, col_i) - (row_i+1, col_i+1) the Area A_i = 1/2 * (col_i + col_i+1) * (row_i - row_i+1)
#                                      n
# The Total Area is therefore A = 1/2 SIGMA (col_i + col_i+1) * (row_i - row_i+1)
#                                      1
# Therefore we can calculate A for Satz of Pick and the OutsideLength (which is R in Satz von Pick) to get I = -A + R/2 + 1
# Here we add all the corners that we are passing

# In the first we loop we save all the corners and the Outside Length
OutsideLength = 0
for line in Data1:
    Length = line[1]
    Dir = Directions[line[0]]
    NewPosition = NextCorner(NewPosition, Dir, Length)
    Corners.append(NewPosition)
    OutsideLength += Length

# In the second loop we calculate the Area of the Polygon via the Shoelace Formula
A = 0
for i, Corner in enumerate(Corners):
    if i < len(Data1):
        row0 = Corners[i][0]
        col0 = Corners[i][1]

        row1 = Corners[i+1][0]
        col1 = Corners[i+1][1]

        A += 1/2*(col0+col1)*(row0-row1)

print("D18 P1 Solution: ", int(-A + OutsideLength/2 + 1))

# PART 2

Corners = [(0,0)]
NewPosition = (0,0)

OutsideLength = 0
for line in Data2:
    Length = line[1]
    Dir = Directions[line[0]]
    NewPosition = NextCorner(NewPosition, Dir, Length)
    Corners.append(NewPosition)
    OutsideLength += Length

A = 0
for i, Corner in enumerate(Corners):
    if i < len(Data2):
        row0 = Corners[i][0]
        col0 = Corners[i][1]

        row1 = Corners[i+1][0]
        col1 = Corners[i+1][1]

        A += 1/2*(col0+col1)*(row0-row1)

print("D18 P2 Solution: ", int(-A + OutsideLength/2 + 1))

        
