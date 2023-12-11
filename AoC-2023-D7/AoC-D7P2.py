
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-2023-D7\AoC-D7.txt") as file:
    for line in file:
        Data.append(line.rstrip())

D1 = []
for line in Data:
    CurrLine = line.split()
    L1 = []
    for symbol in CurrLine[0]:
        L1.append(symbol)
    CurrLine[0] = L1
    D1.append(CurrLine)

CardStrength = {"A": 1, "K": 2, "Q": 3, "J": 99, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

for game in D1:
    CurrHand = game[0]
    gameResult = []
    for singlecard in list(dict.fromkeys(CurrHand)):
        gameResult.append([singlecard, CurrHand.count(singlecard)])
    game.append(gameResult)

    ResultString = ""

    HasJ = False
    Jind = 0
    JAmt = 0
    MaxCard = ""
    MaxVal = 0

    for i, comb in enumerate(gameResult):
        if MaxVal < comb[1] and comb[0] != "J":
            MaxVal = comb[1]
            MaxCard = comb[0]
            MaxIndex = i
        if comb[0] == "J":
            HasJ = True
            JAmt = comb[1]
            Jind = i

    if HasJ == True:
        if game[0] != ["J", "J", "J", "J", "J"]:
            gameResult[MaxIndex][1] += gameResult[Jind][1]
            gameResult.remove(["J", JAmt])

    if len(gameResult) == 1:
        ResultString = "A-FiveAKind"
    elif len(gameResult) == 2:
        n1 = gameResult[0][1]
        n2 = gameResult[1][1]
        if n1 * n2 == 4:
            ResultString = "B-FourAKind"
        elif n1 * n2 == 6:
            ResultString = "C-FullHouse"
    elif len(gameResult) == 3:
        n1 = gameResult[0][1]
        n2 = gameResult[1][1]
        n3 = gameResult[2][1]
        if n1 * n2 * n3 == 3:
            ResultString = "D-ThreeAKind"
        elif n1 * n2 * n3 == 4:
            ResultString = "E-TwoPair"
    elif len(gameResult) == 4:
        ResultString = "F-OnePair"
    elif len(gameResult) == 5:
        ResultString = "G-HighCard"

    StrengthList = []
    for card in CurrHand:
        StrengthList.append(CardStrength[card])
    game.append(StrengthList)

    game.append(ResultString)

SortedD1 = D1
D1.sort(key=lambda x: (x[-1], x[-2][0], x[-2][1], x[-2][2], x[-2][3], x[-2][4]))

games = len(SortedD1)
sol = 0
for i, game in enumerate(SortedD1):
    bid = int(game[1])
    sol = sol + (bid * (games - i))

print("D7 P2 Solution: ", sol)


            





