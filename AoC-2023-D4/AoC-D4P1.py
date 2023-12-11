
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D4-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

TotalSum = 0

delimiters = [" ", ":"]
Cards = []

for card in Data:
    for delimiter in delimiters:
        card = " ".join(card.split(delimiter))
    Cards.append(card.split())

for card in Cards:

    CurrGame = card[1]

    WinningNumbers = []

    i = 2
    while card[i] != "|":

        WinningNumbers.append(int(card[i]))
        i = i + 1

    print("Game ",CurrGame, ": ", card)
    print("Game ",CurrGame, " WinningNumbers: ", WinningNumbers)

    MyNumbers = []

    i = i + 1
    for i in range(i, len(card)):

        MyNumbers.append(int(card[i]))

    print("Game ",CurrGame, " MyNumbers: ", MyNumbers)

    Wins = 0
    for i in range(0, len(MyNumbers)):
        if MyNumbers[i] in WinningNumbers:
            Wins = Wins + 1

    TotalWins = 0
    if Wins > 0:
        TotalWins = 2**(Wins-1)

    print("Amount of Wins: ",Wins, " - Resulting in: ", TotalWins)

    TotalSum = TotalSum + TotalWins

print("Solution:", TotalSum)

    








                    



                    
                    



                        


                   












            



        

            

                
            


        

