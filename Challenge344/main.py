

input = open('input.txt', 'r')
index=0
inputLines = input.readlines()
max = inputLines[0]

inputLines.pop(0)
inputDict = {}

for value in inputLines:
    inputDict['p'+str(index)]=value
    index+=1
# dict(('p'+str(index+=1),v) for v in inputLines)

newList = [k for (k,v) in inputDict.iteritems() if (max in v)]
# print str(max)
print newList
