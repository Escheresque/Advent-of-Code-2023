Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D13\AoC-D13.txt") as file:
    for line in file:
        Data.append(line.rstrip())

nData = []
TempList = []
for i, line in enumerate(Data):
    if line != '' and i != len(Data) - 1:
        TempList.append(line.rstrip())
    elif line.rstrip() == '' or i == len(Data) - 1:
        if i == len(Data) - 1:
            TempList.append(line.rstrip())
        nData.append(TempList)
        TempList = []

    
def isprime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

primes = []
for i in range(2, 100):
    if isprime(i): primes.append(i)

def rowprimes(space):

    RowPrimeList = []
    
    for row in range(0, len(space)):
        fprime = 1
        for col, sym in enumerate(space[row]):
            if sym == "#":
                fprime *= primes[col]

        RowPrimeList.append(fprime)

    return RowPrimeList

def colprimes(space):

    ColPrimeList = []
    for i in range(0, len(space[0])):
        ColPrimeList.append(1)

    for row in range(0, len(space)):
        for col, sym in enumerate(space[row]):
            if sym == "#":
                ColPrimeList[col] *= primes[row]

    return ColPrimeList

def findmirror(space):

    prow = rowprimes(space)
    pcol = colprimes(space)

    rmirr = 0
    for i in range(1, len(prow)):
        if 2*i < len(prow):
            if prow[:i] == prow[i:i+i][::-1]:
                c1 = prow[:i]
                c2 = prow[i:i+i][::-1]
                rmirr = i

        elif prow[i:] == prow[i-(len(prow)-i):i][::-1]:
                d1 = prow[i:]
                d2 = prow[i-(len(prow)-i):i][::-1]
                rmirr = i

    cmirr = 0
    for i in range(1, len(pcol)):

        if 2*i < len(pcol):
            if pcol[:i] == pcol[i:i+i][::-1]:
                a1 = pcol[:i]
                a2 = pcol[i:i+i][::-1]
                cmirr = i

        elif pcol[i:] == pcol[i-(len(pcol)-i):i][::-1]:
                b1 = pcol[i:]
                b2 = pcol[i-(len(pcol)-i):i][::-1]
                cmirr = i

    ret = [cmirr, rmirr]
    return ret

def findmirror2(space, Test):

    prow = rowprimes(space)
    pcol = colprimes(space)

    rmirr = 0
    for i in range(1, len(prow)):
        if 2*i < len(prow):
            if prow[:i] == prow[i:i+i][::-1]:
                c1 = prow[:i]
                c2 = prow[i:i+i][::-1]
                if Test[1] != i:
                    rmirr = i

        elif prow[i:] == prow[i-(len(prow)-i):i][::-1]:
                d1 = prow[i:]
                d2 = prow[i-(len(prow)-i):i][::-1]
                if Test[1] != i:
                    rmirr = i

    cmirr = 0
    for i in range(1, len(pcol)):

        if 2*i < len(pcol):
            if pcol[:i] == pcol[i:i+i][::-1]:
                a1 = pcol[:i]
                a2 = pcol[i:i+i][::-1]
                if i != Test[0]:
                    cmirr = i

        elif pcol[i:] == pcol[i-(len(pcol)-i):i][::-1]:
                b1 = pcol[i:]
                b2 = pcol[i-(len(pcol)-i):i][::-1]
                if i != Test[0]:
                    cmirr = i

    ret = [cmirr, rmirr]
    return ret
def changeStringAtIndex(Str, newLetter, i):

    L = list(Str)

    L[i] = newLetter

    return "".join(L)

D13P1Sol = 0
D13P2Sol = 0
for space in nData:
    Test = findmirror(space)
    D13P1Sol += Test[0] + Test[1]*100
    newRef = False

    for n in range(0, len(space)):
        for m in range(0, len(space[n])):
            if newRef == False:
                newspace = space.copy()
                if newspace[n][m] == ".":
                    newspace[n] = changeStringAtIndex(newspace[n], "#", m)
                else:
                    newspace[n] = changeStringAtIndex(newspace[n], ".", m)
                Test2 = findmirror2(newspace, Test)

                if Test[0] != Test2[0] and Test2[0] != 0:
                    D13P2Sol += Test2[0] + Test2[1]*100
                    newRef = True
                elif Test[1] != Test2[1] and Test2[1] != 0:
                    D13P2Sol += Test2[1]*100
                    newRef = True


print("D13 P1 Solution: ", D13P1Sol)
print("D13 P2 Solution: ", D13P2Sol)





