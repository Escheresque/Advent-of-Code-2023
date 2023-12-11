
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D3-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

TotalSum = 0

print("NEXT TRY ---------------------------------")
for d in range(0, len(Data) - 1):

    CurrSum = 0

    if d != 0 and d != 139:

        for s in range(0, len(Data[d])):

            if Data[d][s] == "*":

                # Middle
                AdjacentNumbers = []

                if Data[d][s-1].isnumeric() == True:
                    LeftNumber = Data[d][s-1]
                    counter = 1
                    while Data[d][s-1-counter].isnumeric() == True:
                        LeftNumber = Data[d][s-1-counter] + LeftNumber
                        counter += 1
                        if s-1-counter == -1:
                            break

                    AdjacentNumbers.append(int(LeftNumber))

                if Data[d][s+1].isnumeric() == True:
                    RightNumber = Data[d][s+1]
                    counter = 1
                    if s+1+counter == 140:
                        break
                    while Data[d][s+1+counter].isnumeric() == True:
                        RightNumber = RightNumber + Data[d][s+1+counter]
                        counter += 1
                        if s+1+counter == 140:
                            break

                    AdjacentNumbers.append(int(RightNumber))

                #Top
                if Data[d-1][s].isnumeric() == False:

                    if Data[d-1][s-1].isnumeric() == True:
                        LeftNumber = Data[d-1][s-1]
                        counter = 1
                        while Data[d-1][s-1-counter].isnumeric() == True:
                            LeftNumber = Data[d-1][s-1-counter] + LeftNumber
                            counter += 1
                            if s-1-counter < 0:
                                break
                        AdjacentNumbers.append(int(LeftNumber))
                    
                    if Data[d-1][s+1].isnumeric() == True:
                        RightNumber = Data[d-1][s+1]
                        counter = 1
                        while Data[d-1][s+1+counter].isnumeric() == True:
                            RightNumber = RightNumber + Data[d-1][s+1+counter]
                            counter += 1
                            if s+1+counter == 140:
                                break
                        AdjacentNumbers.append(int(RightNumber))

                elif Data[d-1][s].isnumeric() == True:
                    if Data[d-1][s+1].isnumeric() == True and Data[d-1][s-1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d-1][s-1:s+2]))
                    elif Data[d-1][s+1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d-1][s:s+3].replace(".","").replace("#","")))
                    elif Data[d-1][s-1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d-1][s-3:s+1].replace(".", "").replace("#","")))
                
                #Bottom
                if Data[d+1][s].isnumeric() == False:

                    if Data[d+1][s-1].isnumeric() == True:
                        LeftNumber = Data[d+1][s-1]
                        counter = 1
                        while Data[d+1][s-1-counter].isnumeric() == True:
                            LeftNumber = Data[d+1][s-1-counter] + LeftNumber
                            counter += 1
                            if s-1-counter < 0:
                                break
                        AdjacentNumbers.append(int(LeftNumber))
                    
                    if Data[d+1][s+1].isnumeric() == True:
                        RightNumber = Data[d+1][s+1]
                        counter = 1
                        while Data[d+1][s+1+counter].isnumeric() == True:
                            RightNumber = RightNumber + Data[d+1][s+1+counter]
                            counter += 1
                            if s+1+counter == 140:
                                break
                        AdjacentNumbers.append(int(RightNumber))

                elif Data[d+1][s].isnumeric() == True:
                    if Data[d+1][s+1].isnumeric() == True and Data[d+1][s-1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d+1][s-1:s+2]))
                    elif Data[d+1][s+1].isnumeric() == False and Data[d+1][s-1].isnumeric() == False:
                        AdjacentNumbers.append(int(Data[d+1][s]))
                    elif Data[d+1][s+1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d+1][s:s+3].replace(".","").replace("#","")))
                    elif Data[d+1][s-1].isnumeric() == True:
                        AdjacentNumbers.append(int(Data[d+1][s-3:s+1].replace(".", "").replace("#","")))

                Product = 0
                if len(AdjacentNumbers) == 2:
                    Product = AdjacentNumbers[0] * AdjacentNumbers[1]
                    TotalSum = TotalSum + Product

                print("Row: ",d+1," Position:", s, "AdjNum: ", AdjacentNumbers, "Product:", Product, "NewSum:", TotalSum)


print("TotalSum:",TotalSum)


                    



                    
                    



                        


                   












            



        

            

                
            


        

