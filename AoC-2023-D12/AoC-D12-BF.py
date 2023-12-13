##############################################################################################################

### PLEASE READ ###

### This is horrible code that at least works.. but takes a long time in some cases (1 out of 20 rows is "too long")
### A friend of mine works at a company that has a big ass computer
### So I asked him to run this code on that PC
### That's how I got the answer for D12P2
### I'm not proud of it but sometimes its better to have more power :) 

import numpy as np

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D12\AoC-D12.txt") as file:
    for line in file:
        TempList = ["", ""]
        FirstNumber = True
        for i, l in enumerate(line):
            if l.isnumeric() and FirstNumber == True:
                TempList[0] = list(line[:i].rstrip())
                TempList[1] = list(map(int, line[i:].replace("\n", "").split(",")))
                FirstNumber = False
        Data.append(TempList)

nData = Data.copy()
for i, line in enumerate(Data):
    newList = []
    for s in line[0]:
        if s == "?":
            newList.append(0)
        elif s == ".":
            newList.append(-1)
        else:
            newList.append(1)
    nData[i][0] = newList

P2Data = []
for line in nData:
    code = line[0]
    key = line[1]

    newcode = []
    newkey = []
    for i in range(0, 5):
        for c in code:
            newcode.append(c)
        for k in key:
            newkey.append(k)
        newcode.append(0)

    newcode.pop()
    P2Data.append([newcode, newkey])

def CheckPossibility(att, code):
    isValid = True
    newList = [a*b for a,b in zip(att, code)]

    if sum(newList) != sum([abs(ele) for ele in newList]):
        isValid = False

    return isValid

def Transport(att, key, bn, code):

    for i in range(0, len(att)):
        if att[i] == 0:
            left = i
            break

    right = len(att) - sum(key[bn + 1:]) - len(key[bn + 1:]) - key[bn] + 1

    if bn == len(key) - 1:
        right = len(att) - key[bn] + 1

    tries = []

    if left == len(att) - key[bn]:
        t = att.copy()
        t[left:] = [1] * key[bn]
        if CheckPossibility(t, code):
            tries.append(t)

    elif left == 0 and right == 0:
        t = att.copy()
        t[:key[bn]] = [1] * key[bn]
        if CheckPossibility(t, code):
            tries.append(t)

    elif left + key[bn] < len(att):
        for i in range(left, right):
            t = att.copy()
            if i == 0:
                t[:key[bn]] = [1] * key[bn]
                t[key[bn]] = -1
            else:
                t[left:i] = [-1] * (i-left)
                t[i:i+key[bn]] = [1] * key[bn]
                if i + key[bn] < len(t):
                    t[i+key[bn]] = -1

            if bn == len(key) - 1:
                for d in range(0, len(t)):
                    if t[d] == 0:
                        t[d] = -1

            if CheckPossibility(t, code):
                tries.append(t)

    return tries

def TransportList2(atts, key, bn, code):

    ReturnList = []
    attcounter = 0
    for att in atts:
        attcounter += 1
        if attcounter % 10000 == 0 and attcounter > 0:
            print("Loop:", counter, "/", len(Data), " - ", bn, ".", len(key), " -- ", attcounter, "/", len(atts))
        ReturnList.extend(Transport(att,key,bn,code))

    return ReturnList

D12Sol = 0
counter = 1
for p, line in enumerate(P2Data):
    code = line[0]
    key = line[1]

    currtest = []
    for f in range(0, len(code)):
        currtest.append(0)

    it = [currtest.copy()]

    for i, k in enumerate(key):

        it = TransportList2(it, key, i, code)
    
    D12Sol += len(it)

    counter += 1

print("D12 Solution: ", D12Sol)





