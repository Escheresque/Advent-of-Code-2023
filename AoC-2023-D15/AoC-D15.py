Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D15\AoC-D15.txt") as file:
    for line in file:
        Data.append(line.rstrip().split(","))

d1 = {i: chr(i) for i in range(128)}
d2 = {v: k for k, v in d1.items()}

def Gleichheit(boxes, b, newEntry):

    work = boxes[b].copy()

    label = newEntry[0]

    if work == []:
        work = [newEntry]
    else:
        alreadyInside = False
        for i, lenses in enumerate(work):
            if lenses[0] == label:
                alreadyInside = True
                loc = i

        if alreadyInside == True:
            work[loc] = newEntry

        else:
            work.append(newEntry)

    boxes[b] = work

    return boxes

def Minus(boxes, b, label):

    work = boxes[b].copy()

    for i, lenses in enumerate(work):
        if lenses[0] == label:
            work.remove(work[i])

    boxes[b] = work

    return boxes

def HashFunction(prev, s):
    return ((prev + d2[s]) * 17) % 256

D15P1Sol = 0
for string in Data[0]:
    it = 0
    for l in string:
        it = HashFunction(it, l)
    D15P1Sol += it

print("D15 P1 Solution: ", D15P1Sol)

Boxes = []
for i in range(0, 256): Boxes.append([])

for string in Data[0]:
    hashval = 0
    label = ""
    for i, l in enumerate(string):
        if l != "=" and l != "-" and l.isnumeric() == False:
            hashval = HashFunction(hashval, l)
            label += l
            
        elif l == "=":
            focallength = string[i+1]
            Boxes = Gleichheit(Boxes, hashval, [label, focallength])

        elif l == "-":
            Boxes = Minus(Boxes, hashval, label)

D15P2Sol = 0
for b, box in enumerate(Boxes):

    for l, lens in enumerate(box):
        focPower = (1 + b)*(1 + l)*(int(lens[1]))
        D15P2Sol += focPower

print("D15 P2 Solution: ", D15P2Sol)



