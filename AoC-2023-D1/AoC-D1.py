
# First we load the data from a text file

def P1Finder(string):
    Temp = []
    for l in string:
        if l.isnumeric(): 
            Temp.append(l)
    
    return int(Temp[0] + Temp[-1])

def P2Finder(string):

    string = string.replace("one", "o1e")
    string = string.replace("two", "t2o")
    string = string.replace("three", "t3e")
    string = string.replace("four", "f4r")
    string = string.replace("five", "f5e")
    string = string.replace("six", "s6x")
    string = string.replace("seven", "s7n")
    string = string.replace("eight", "e8t")
    string = string.replace("nine", "n9e")

    return P1Finder(string)

Data = []
D1P1Sol = 0
D1P2Sol = 0

with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\D1\AoC-D1.txt") as file:
    for line in file:
        D1P1Sol += P1Finder(line.rstrip())
        D1P2Sol += P2Finder(line.rstrip())
        Data.append(line.rstrip())

print("D1 P1 Solution: ", D1P1Sol)
print("D1 P2 Solution: ", D1P2Sol)




            

                        


        






