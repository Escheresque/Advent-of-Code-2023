
Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\Advent of Code 2023\AoC-D5-Data.txt") as file:
    for line in file:
        Data.append(line.rstrip())

Seeds = []
SeedSoilMap = []
SoilFertMap = []
FertWaterMap = []
WaterLightMap = []
LightTempMap = []
TempHumiMap = []
HumiLocMap = []

for line in Data:
    if len(line) > 0:
        if line[0].isnumeric() == False:
            if line == "seeds:":
                Seeds = Data[Data.index(line) + 1].split()
            elif line == "seed-to-soil map:":
                TempList = Data[Data.index(line) + 1:17]
                for triple in TempList:
                    SeedSoilMap.append(triple.split())
            elif line == "soil-to-fertilizer map:":
                TempList = Data[Data.index(line) + 1:40]
                for triple in TempList:
                    SoilFertMap.append(triple.split())
            elif line == "fertilizer-to-water map:":
                TempList = Data[Data.index(line) + 1:90]
                for triple in TempList:
                    FertWaterMap.append(triple.split())
            elif line == "water-to-light map:":
                TempList = Data[Data.index(line) + 1:131]
                for triple in TempList:
                    WaterLightMap.append(triple.split())
            elif line == "light-to-temperature map:":
                TempList = Data[Data.index(line) + 1:149]
                for triple in TempList:
                    LightTempMap.append(triple.split())
            elif line == "temperature-to-humidity map:":
                TempList = Data[Data.index(line) + 1:158]
                for triple in TempList:
                    TempHumiMap.append(triple.split())
            elif line == "humidity-to-location map:":
                TempList = Data[Data.index(line) + 1:191]
                for triple in TempList:
                    HumiLocMap.append(triple.split())

AllMaps = [SeedSoilMap, SoilFertMap, FertWaterMap, WaterLightMap, LightTempMap, TempHumiMap, HumiLocMap]

SeedRanges = []
for i in range(0, len(Seeds), 2):
    SeedRanges.append([int(Seeds[i]), int(Seeds[i]) + int(Seeds[i + 1]) - 1])

def GetRanges(XXMap):

    InputRanges = []
    OutputRanges = []
    for triple in XXMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        InputRanges.append([s, s+r-1])
        OutputRanges.append([d, d+r-1])

    return [InputRanges, OutputRanges]

# This is not nice but I want to sleep
SeedSoilRanges = GetRanges(SeedSoilMap)
SoilFertRanges = GetRanges(SoilFertMap)
FertWaterRanges = GetRanges(FertWaterMap)
WaterLightRanges = GetRanges(WaterLightMap)
LightTempRanges = GetRanges(LightTempMap)
TempHumiRanges = GetRanges(TempHumiMap)
HumiLocRanges = GetRanges(HumiLocMap)

# Okay real quick the idea
# We have the cutter function below
# and a Mapper function

# The cutter function takes a start range (e.g. [0, 10]) and if we have maps somewhere inbetween (e.g. [2,4] and [6,7]) we get new ranges (e.g. [[0,1],[2,4],[5,5],[6,7],[7,10]])
# Since by construction these new ranges are all either in a Mapping Range or not, we have the mapping function that maps the according range intervals to new intervals.
# Rinse and repeat and we get to the end!

def Cutter(StartRanges, MapRanges):

    SplitInputRanges = []

    for sRange in StartRanges:

        s1 = int(sRange[0])
        s2 = int(sRange[1])
        Cuts = [s1]

        for InputRange in MapRanges[0]:

            i1 = int(InputRange[0])

            if i1 >= s1 and i1 <= s2:
                if i1 == s1:
                    Cuts.append(i1)
                    Cuts.append(i1+1)
                elif i1 == s2:
                    Cuts.append(i1-1)
                    Cuts.append(i1)
                else:
                    Cuts.append(i1)
                    Cuts.append(i1+1)
            
        for InputRange in MapRanges[0]:

            i2 = int(InputRange[1])

            if i2 >= s1 and i2 <= s2:
                if i2 == s1:
                    Cuts.append(i2)
                    Cuts.append(i2+1)
                elif i2 == s2:
                    print("")
                else:
                    Cuts.append(i2)
                    Cuts.append(i2+1)

        Cuts.append(s2)
        Cuts.sort()

        for i in range(0, len(Cuts) - 1, 2):
            if Cuts[i] == 78 and Cuts[i+1] == 76:
                print("Stop")
            SplitInputRanges.append([Cuts[i], Cuts[i+1]])

    return SplitInputRanges

def Mapper(StartRanges, MapRanges):

    OutputRanges = []

    for sRange in StartRanges:

        s1 = sRange[0]
        s2 = sRange[1]

        inRange = False
        for i in range(0, len(MapRanges[0])):

            i1 = int(MapRanges[0][i][0])
            i2 = int(MapRanges[0][i][1])

            o1 = int(MapRanges[1][i][0])
            o2 = int(MapRanges[1][i][1])

            if s1 >= i1 and s1 <= i2:
                n1 = o1 + (s1 - i1)
                inRange = True
                n2 = o1 + (s2 - i1)
                OutputRanges.append([n1, n2])

        if inRange == False:
            OutputRanges.append(sRange)

    return OutputRanges

# I know this is not nice, but its midnight and I want to go to sleep
C1 = Cutter(SeedRanges, SeedSoilRanges)
M1 = Mapper(C1, SeedSoilRanges)

C2 = Cutter(M1, SoilFertRanges)
M2 = Mapper(C2, SoilFertRanges)

C3 = Cutter(M2, FertWaterRanges)
M3 = Mapper(C3, FertWaterRanges)

C4 = Cutter(M3, WaterLightRanges)
M4 = Mapper(C4, WaterLightRanges)

C5 = Cutter(M4, LightTempRanges)
M5 = Mapper(C5, LightTempRanges)

C6 = Cutter(M5, TempHumiRanges)
M6 = Mapper(C6, TempHumiRanges)

C7 = Cutter(M6, HumiLocMap)
M7 = Mapper(C7, HumiLocRanges)

# Listen I know this is probably the worst way you can find the min, but it is midnight and I want to go to sleep
maxi = 0
for tuple in M7:
    maxi = max(maxi, tuple[0], tuple[1])

minny = maxi
for tuple in M7:
    minny = min(minny, tuple[0], tuple[1])

print("Solution: ", minny)
    



    





    








                    



                    
                    



                        


                   












            



        

            

                
            


        

