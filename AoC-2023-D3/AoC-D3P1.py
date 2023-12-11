
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D3-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

# Jede Zeile hat 140 Zeichen
# zunächst müssen wir herausfinden, wo die Zahlen sind um dann "um Sie herum" zu schauen, ob Sie ein Symbol haben
# Wenn ja, dann zählt diese Zahl zur Gesamtsumme

DataNumbers = []
DataIndices = []

for code in Data:

    CodeNumbers = []
    CodeIndices = []

    for i in range(0, len(code)):

        if (code[i].isnumeric() == True and i == 0) or (code[i].isnumeric() == True and code[i-1].isnumeric() == False and i!=0):

            NewNumber = code[i]
            Counter = 1
            
            while i + Counter < 140:

                if code[i + Counter].isnumeric() == True:

                    NewNumber = NewNumber + code[i + Counter]

                if code[i + Counter].isnumeric() == False:
                    break

                Counter += 1

            CodeNumbers.append(int(NewNumber))
            CodeIndices.append([i, i + Counter ])

    DataNumbers.append(CodeNumbers)
    DataIndices.append(CodeIndices)

print(DataNumbers)
print(DataIndices)

TotalSum = 0

for d in range(0, len(Data) - 1):

    CurrSum = 0

    if d != 0 and d != 139:

        print("Step ",d, " Start TotalSum: ", TotalSum)

        for t in range(0, len(DataIndices[d])):

            StartIndex = DataIndices[d][t][0]
            EndIndex = DataIndices[d][t][1]

            CountNumber = 0

            if EndIndex < 139:
                for i in range(StartIndex - 1, EndIndex + 1):
                    for j in [d-1, d+1]:
                        if Data[j][i] != "." and Data[j][i].isnumeric() == False:
                            CountNumber += 1
            else:
                for i in range(StartIndex - 1, EndIndex):
                    for j in [d-1, d+1]:
                        if Data[j][i] != "." and Data[j][i].isnumeric() == False:
                            CountNumber += 1

            if Data[d][StartIndex - 1] != "." and Data[d][StartIndex - 1].isnumeric() == False:
                CountNumber += 1

            if EndIndex + 1 < 139:
                if Data[d][EndIndex] != "." and Data[d][EndIndex].isnumeric() == False:
                    CountNumber += 1

            if CountNumber > 0:
                CurrSum += int(DataNumbers[d][t])
                TotalSum = TotalSum + int(DataNumbers[d][t])

    print("Step ",d, " End TotalSum: ", TotalSum)

TotalSum += (283 + 867) + (472 + 451 + 904)
print("TotalSum: ", TotalSum)
                
Test = 370 + 48 + 456 + 424 + 341 + 554 + 807 + 571 + 971 + 958 + 166
print(Test)
Test2 = 159+539+73+954+7+405+31
print(Test2)





                   












            



        

            

                
            


        

