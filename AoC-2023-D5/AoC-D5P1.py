
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

SeedRanges = []
for i in range(0, len(Seeds), 2):
    SeedRanges.append([int(Seeds[i]), int(Seeds[i]) + int(Seeds[i + 1]) - 1])

Soils = []          
for Seed in Seeds:
    p = int(Seed)
    InRanges = False
    for triple in SeedSoilMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Soils.append(d + v)
            InRanges = True

    if InRanges == False:
        Soils.append(p)

Ferts = []
for Soil in Soils:
    p = int(Soil)
    InRanges = False
    for triple in SoilFertMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Ferts.append(d + v)
            InRanges = True

    if InRanges == False:
        Ferts.append(p)

Waters = []
for Fert in Ferts:
    p = int(Fert)
    InRanges = False
    for triple in FertWaterMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Waters.append(d + v)
            InRanges = True

    if InRanges == False:
        Waters.append(p)

Lights = []
for Water in Waters:
    p = int(Water)
    InRanges = False
    for triple in WaterLightMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Lights.append(d + v)
            InRanges = True

    if InRanges == False:
        Lights.append(p)
        

Temps = []
for Light in Lights:
    p = int(Light)
    InRanges = False
    for triple in LightTempMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Temps.append(d + v)
            InRanges = True
    
    if InRanges == False:
        Temps.append(p)

Humis = []
for Temp in Temps:
    p = int(Temp)
    InRanges = False
    for triple in TempHumiMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Humis.append(d + v)
            InRanges = True

    if InRanges == False:
        Humis.append(p)

Locs = []
for Humi in Humis:
    p = int(Humi)
    InRanges = False
    for triple in HumiLocMap:
        d = int(triple[0])
        s = int(triple[1])
        r = int(triple[2])

        if p >= s and p < s+r:
            v = p - s
            Locs.append(d + v)
            InRanges = True

    if InRanges == False: 
        Locs.append(p)

print("Locs: ", Locs)
print("Solution: ", min(Locs))
            
print("End")

        



    





    








                    



                    
                    



                        


                   












            



        

            

                
            


        

