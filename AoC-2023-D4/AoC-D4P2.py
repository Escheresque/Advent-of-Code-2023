
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D4-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

TotalSum = 0

delimiters = [" ", ":"]
Cards = []
OriginalCards = []
OriginalCardsWins = []
CardCount = []

testcounter = 0

for card in Data:
    for delimiter in delimiters:
        card = " ".join(card.split(delimiter))
    Cards.append(card.split())
    OriginalCards.append(card.split())

for card in Cards:

    CurrGame = card[1]
    WinningNumbers = []

    i = 2
    while card[i] != "|":

        WinningNumbers.append(int(card[i]))
        i = i + 1

    MyNumbers = []

    i = i + 1
    for i in range(i, len(card)):

        MyNumbers.append(int(card[i]))

    Wins = 0
    for i in range(0, len(MyNumbers)):
        if MyNumbers[i] in WinningNumbers:
            Wins = Wins + 1

    OriginalCardsWins.append(Wins)
    CardCount.append(1)

for i in range(0, len(OriginalCardsWins)):
    print("CurrStep: ",i)
    for k in range(0, CardCount[i]):
        for j in range(1, OriginalCardsWins[i]+1):
            if j > 215:
                break
            CardCount[i + j] = CardCount[i + j] + 1

Sol = sum(CardCount)

print("Solution:", Sol)

    








                    



                    
                    



                        


                   












            



        

            

                
            


        

