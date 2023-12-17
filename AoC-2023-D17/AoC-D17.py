from heapq import heappush, heappop

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2023\AoC-2023-D17\AoC-D17.txt") as file:
    for line in file:
        Data.append(list(map(int, list(line.rstrip()))))

# This solution was deducted by watching 4 Videos on Dijkstra's Algorithm, learning about heaps and watching someone else explain his solution.
# At the end of this file you will find all the sources if you are interested
# I was not able to solve this completely on my own (as with other Problems). 

# A min-heap is a binary tree where each "child" is greater than their "parent". Here is an example:
#       7    As we can see, in each step the values are getting lower.
#   3        Technically, this is exactly the same as we have with the heatloss. With each step our "incurred heat loss" gets bigger. 
#       9    And, in a sense, each position has three childred - which are the directions it can still go (don't forget that we are not able to go backwards)
# 1          Of Course, our "graph" looks a bit different, but we can use the functions heappop() and heappush() to our advantage. 
#       6
#   5
#       7

# We also use the concept of a priority queue: Each element in a priority queue has an assiciated priority.
# Elements with a high priority are served before elements with a low priority. 
# This idea will become useful since our algorithm tries to find the bottom right corner.
# Since our priority queue always starts with the "lower heatloss cost" way to get somewhere, the first time we find the end point is also the most efficient way.
        
# At the same time we use DIJKSTRA's ALGORITH to basically get the "lowest cost" way to the end point.
# First we initialize by giving every neighbor a "cost" of 999999 (or basically infinite)
# Dijkstra's Algorithm starts at one specific point and checks all the direct neighbours. For each sepcific neighbor we calculate the cost to get there and
# give the neighbor the new cost min(PrevCost, NewCost). If the minimum cost was changed, we also note "from where" we came to get this minimum cost
# Then we note that we have already finished to check each neighbor for the starting value.
# In the next step we go to the lowest cost neighbor and do the same: check all costs (new cost will be cost to get to this point + cost to get to neighbor), look if a new minimum has been created, if yes, note the current node as predecessor
# and then note the current node in the "AlreadySeen" list.
# This repeats until we have seen every knot. The cost of each knot is now the lowest it can be (through our minimization) and we now how to get there since we noted the predecessor of this min cost.
        
# This is basically the algorithm we have down below, just with the added Priority Queue which always gives us the lowest cost way first. 

# This set here will contain all the coordinates with the directions we came to from here and the amount of steps we have taken so far
AlreadySeen = set()

# PriorityQ consists of heatloss, current Row, current Col, current Direction Row, current Direction Col, times moved in one direction
PQ = [(0, 0, 0, 0, 0, 0)]

# while PQ basically just means that while PQ is not empty we should continue calculating. Since PQ is never empty this algorithm will go on until we get the one break statement. 
while PQ:

    # After appending something new below, the Priority Queue will always have the coordinates with the lowest incurred heatloss at the top. 
    # With heappop we REMVOE this from the Priority Queue, but at the same time we read the data that we are now popping for the next step.
    # That means in each iteration of this algorithm we take the lowest heatloss so far in all the directions, save it ordered by the heatloss in the Priority Queue
    # and the check the new first one in the next directions. 
    heatloss, currrow, currcol, dirrow, dircol, onedirsteps = heappop(PQ)

    # As previously mentioned the algorithm should immediately break when we find the end point
    if currrow == len(Data) - 1 and currcol == len(Data[0]) - 1: 
        print("D17 P1 Solution: ", heatloss)
        break

    # Here we control for the boundaries. If our algorithm wants to go out of bounds, we immeadiately go to the next try
    if currrow < 0 or currrow >= len(Data) or currcol < 0 or currcol >= len(Data[0]):
        continue

    # Here we watch if we have already seen these coordinates and this direction. Since it can't be efficient to make a loop we also stop checking these ones
    if (currrow, currcol, dirrow, dircol, onedirsteps) in AlreadySeen:
        continue

    # Now we now that we have not been at the current location. Therefore we add it to AlreadySeen in case that we get there again.
    AlreadySeen.add((currrow, currcol, dirrow, dircol, onedirsteps))

    # The next two blocks are basically for testing the new directions. 

    # Here we move in one direction if the steps in that one direction is smaller than three.
    # Here we also only move in the direction we were already moving. This can only happen up to onedirsteps < 3 as stated in the Problem
    # The [dirrow, dircol] != [0,0] is for the Start Case
    if onedirsteps < 3 and [dirrow, dircol] != [0,0]:
        nextrow = currrow + dirrow
        nextcol = currcol + dircol
        # Here we first check if we are still in bounds of our array
        # if we are in the bounds of the array, we add to our priority queue the data of our last move.
        # That means the currenct heatloss we experience, the next coordinates, the last direction and the amount of steps we have taken in this direction.
        if 0 <= nextrow < len(Data) and 0 <= nextcol < len(Data[0]):
            heappush(PQ, (heatloss + Data[nextrow][nextcol], nextrow, nextcol, dirrow, dircol, onedirsteps + 1))

    # Here we check the new directions, which are all 4 directions across one specific step
    # if the new direction should be the same as the old one, we don't do this here since we have already done it before right above this
    # if the new direction is the negative of the last direction, we also won't execute this, since we can't go backwards. 
    for newdirrow, newdircol in [[0,1],[1,0],[0,-1],[-1,0]]:
        if [newdirrow, newdircol] != [dirrow, dircol] and [newdirrow, newdircol] != [-dirrow, -dircol]:
            nextrow = currrow + newdirrow
            nextcol = currcol + newdircol
            # Similar to the above check, we look if the new directions are still in bounds.
            # and the same as before, we also add to the Priority Queue the heatloss we experience, the next coordinates and the last direction
            # additionally, since we are now moving in a different direction than before, we also put onedirsteps at 1 
            if 0 <= nextrow < len(Data) and 0 <= nextcol < len(Data[0]):
                heappush(PQ, (heatloss + Data[nextrow][nextcol], nextrow, nextcol, newdirrow, newdircol, 1))

    # Now that we have checked the new directions and we have pushed them to the Priority Queue our iteration is done.
    # The Priority Queue now includes the heatloss we occured to get to a specific point from a specific location.
    # Since we are using the heappush() function, the lower the heatloss, the further front we add the new information
    # Since we added something to PQ, our while-Loop will now take those next steps. 
    # Since the While loop starts with the heappop() function, it also uses the combination with the lowest heatloss first. 
                

# HERE NOW PART 2 - Which is basically the same algorithm, just with some extras:
                
AlreadySeen = set()
PQ = [(0, 0, 0, 0, 0, 0)]

while PQ:

    heatloss, currrow, currcol, dirrow, dircol, onedirsteps = heappop(PQ)

    # The first difference to aboves algorith is here: we can only stop at the end point if we have already walked at least 4 steps. 
    if currrow == len(Data) - 1 and currcol == len(Data[0]) - 1 and onedirsteps >= 4: 
        print("D17 P2 Solution: ", heatloss)
        break

    if currrow < 0 or currrow >= len(Data) or currcol < 0 or currcol >= len(Data[0]):
        continue

    if (currrow, currcol, dirrow, dircol, onedirsteps) in AlreadySeen:
        continue

    AlreadySeen.add((currrow, currcol, dirrow, dircol, onedirsteps))

    # Here is the second change: since we can now move for a maximum of ten steps in one direction, we have to account for that
    if onedirsteps < 10 and [dirrow, dircol] != [0,0]:
        nextrow = currrow + dirrow
        nextcol = currcol + dircol
        if 0 <= nextrow < len(Data) and 0 <= nextcol < len(Data[0]):
            heappush(PQ, (heatloss + Data[nextrow][nextcol], nextrow, nextcol, dirrow, dircol, onedirsteps + 1))

    # The last change is that here we have the condition, that we must have traveled at least 4 steps before being able to make a turn.
    # the [dirrow, dircol] == [0,0] case is again for the start.
    if onedirsteps >= 4 or [dirrow, dircol] == [0,0]:
        for newdirrow, newdircol in [[0,1],[1,0],[0,-1],[-1,0]]:
            if [newdirrow, newdircol] != [dirrow, dircol] and [newdirrow, newdircol] != [-dirrow, -dircol]:
                nextrow = currrow + newdirrow
                nextcol = currcol + newdircol
                if 0 <= nextrow < len(Data) and 0 <= nextcol < len(Data[0]):
                    heappush(PQ, (heatloss + Data[nextrow][nextcol], nextrow, nextcol, newdirrow, newdircol, 1))

# Sources:
# What is a heap: https://www.youtube.com/watch?v=0wPlzMU-k00
# What are heap methods: https://www.youtube.com/watch?v=pAU21g-jBiE
# heappush() and heappop() from the heapq library: https://docs.python.org/3/library/heapq.html#basic-examples

# Dijkstra's Algorithm: https://www.youtube.com/watch?v=KiOso3VE-vI&t=314s


                
            
