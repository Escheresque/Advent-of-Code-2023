
# First we load the data from a text file
Data = []

with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D2-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

# The Bag has been loaded with 12 red cubes, 13 green cubes and 14 blue cubes.
# Which Games would be possibe?

CurrGame = 1
TotalPower = 0

for game in Data:

    GamePower = 0
    MinR = 0
    MinG = 0
    MinB = 0

    SplitGame = []
    SplitGame.append(game.split(";"))

    print(CurrGame,"----------------------GAME:",game)

    for subgame in SplitGame:

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

            CurrBlue = int(CurrBlue)
            CurrRed = int(CurrRed)
            CurrGreen = int(CurrGreen)

            if CurrBlue > MinB:
                MinB = CurrBlue
            
            if CurrRed > MinR:
                MinR = CurrRed

            if CurrGreen > MinG:
                MinG = CurrGreen

    # Here we add the GamePower
    GamePower = MinB * MinR * MinG
    TotalPower = TotalPower + GamePower

    print("CurrGame:", CurrGame, "GamePower", GamePower, "=", MinB, "*", MinR, "*", MinG,"--TotalPower:", TotalPower)
    CurrGame = CurrGame + 1

print("Solution: ",TotalPower)

            

                        


        






