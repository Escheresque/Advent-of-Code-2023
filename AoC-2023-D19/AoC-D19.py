from copy import deepcopy
Maps = []
Parts = []
EmptyRow = False

Maps = {"Init": "First"}

class PartClass:
    def __init__(self, xval, mval, aval, sval):
        self.xval = xval
        self.mval = mval
        self.aval = aval
        self.sval = sval

with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D19\AoC-D19.txt") as file:
    for line in file:

        if EmptyRow == False:
            line = line.replace("{", ",")
            line = line.replace("}", ",")
            
            if line == "\n":
                EmptyRow = True
                continue

            tline = line.rstrip().split(",")
            Maps[tline[0]] = tline[1:len(tline) - 1]

        if EmptyRow == True:
            line = line.replace("{", ",")
            line = line.replace("}", ",")
            
            Parts.append(line.rstrip().split(",")[1:5])

def InterpretMaps(partdict, MapList):

    for map in MapList:

            if "<" in map:

                temp = map.replace(":","<")
                temp = temp.split("<")

                check = temp[0]
                value = int(temp[1])
                dest = temp[2]

                if partdict[check] < value:
                    return dest
                
            elif ">" in map:

                temp = map.replace(":",">")
                temp = temp.split(">")

                check = temp[0]
                value = int(temp[1])
                dest = temp[2]

                if partdict[check] > value:
                    return dest
                
            else:

                return map

D19P1Sol = 0
for part in Parts:

    print("Checking", part)

    xmasdict = {}
    for p in part:
        p = p.split("=")
        xmasdict[p[0]] = int(p[1])

    NextDest = "in"
    while NextDest != "R" or NextDest != "A":

        NextDest = InterpretMaps(xmasdict, Maps[NextDest])

        if NextDest == "A":
            for key in list(xmasdict.keys()):
                D19P1Sol += xmasdict[key]
            break
        elif NextDest == "R":
            break

print("D19 P1 Solution: ", D19P1Sol)

# Part 2

Vals = []
Valid = {"x": [1, 4000], "m":[1, 4000], "a": [1, 4000], "s": [1, 4000]}

it = [("in", Valid)]

while len(it) > 0:

    print(it)

    label, Valid = it.pop()

    for map in Maps[label]:

        if ":" in map:

            if "<" in map:

                thiscondition = deepcopy(Valid)

                temp = map.replace(":","<")
                temp = temp.split("<")

                check = temp[0]
                value = int(temp[1])
                dest = temp[2]

                thiscondition[check] = [thiscondition[check][0], value - 1]
                Valid[check] =[value, Valid[check][1]]

                if dest in ["A", "R"]:
                    if dest == "A":
                        Vals.append(thiscondition.copy())
                else:
                    it.append([dest, thiscondition.copy()])

            elif ">" in map:

                thiscondition = deepcopy(Valid)

                temp = map.replace(":",">")
                temp = temp.split(">")

                check = temp[0]
                value = int(temp[1])
                dest = temp[2]

                thiscondition[check] = [value + 1, thiscondition[check][1]]
                Valid[check] = [Valid[check][0], value]

                if dest in ["A", "R"]:
                    if dest == "A":
                        Vals.append(thiscondition.copy())
                else:
                    it.append([dest, thiscondition.copy()])

        else:
            if map in ["A", "R"]:
                if map == "A":
                    Vals.append(Valid.copy())
            else:
                it.append([map, Valid.copy()])
                
                          
D19P2Sol = 0
for val in Vals:
    comb = 1
    for v in val.values():
        comb *= v[1] - v[0] + 1
    D19P2Sol += comb

print("D19 P2 Solution:", D19P2Sol)

        













