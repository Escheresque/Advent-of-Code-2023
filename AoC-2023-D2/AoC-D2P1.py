
# First we load the data from a text file
Data = []

with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\D2\AoC-D2.txt") as file:
    for line in file:
        Data.append(line.rstrip())

# The Bag has been loaded with 12 red cubes, 13 green cubes and 14 blue cubes.
# Which Games would be possibe?

MaxR = 12
MaxG = 13
MaxB = 14

IDSum = 0
CurrGame = 1

for game in Data:
    SplitGame = []
    SplitGame.append(game.split(";"))

    print(CurrGame,"----------------------GAME:",game)
    print("-------------------CurrSum:",IDSum)
    isValid = True

    for subgame in SplitGame:

        # Does the whole subgame work?

        for stringgame in subgame:
            stringgame = stringgame.replace(" blue", "b")
            stringgame = stringgame.replace(" green", "g")
            stringgame = stringgame.replace(" red", "r")

            CurrBlue = 0
            CurrGreen = 0
            CurrRed = 0

            stringgame = stringgame.replace(" ", "#")

            for i in range(0, len(stringgame)):
                if stringgame[i] == "b":
                    if stringgame[i-2] != "#":
                        CurrBlue = stringgame[i-2:i]
                    else:
                        CurrBlue = stringgame[i-1]
            
                if stringgame[i] == "r":
                    if stringgame[i-2] != "#":
                        CurrRed = stringgame[i-2:i]
                    else:
                        CurrRed = stringgame[i-1]

                if stringgame[i] == "g":
                    if stringgame[i-2] != "#":
                        CurrGreen = stringgame[i-2:i]
                    else:
                        CurrGreen = stringgame[i-1]

            

            if int(CurrRed) > MaxR or int(CurrBlue) > MaxB or int(CurrGreen) > MaxG:
                isValid = False

    if isValid == True:
        IDSum = IDSum + CurrGame
    else:
        
    CurrGame = CurrGame + 1


            

                        


        






