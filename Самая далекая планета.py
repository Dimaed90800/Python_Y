from math import pi
 
def findFarthestOrbit(listOfOrbits):
    return max([orbit for orbit in listOfOrbits if orbit[0] != orbit[1]], key=lambda x: pi * x[0] * x[1])
 
 
listOfOrbits = [(1, 3),(2.5, 10),(7, 2),(6, 6),(4, 3)]
 
print(findFarthestOrbit(int(listOfOrbits)))