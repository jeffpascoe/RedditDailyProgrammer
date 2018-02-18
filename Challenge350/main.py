
with open('/Users/JeffPascoe/Documents/Github Projects/RedditDailyProgrammer/Challenge350/input.txt') as f:
    shelfList = f.readline().split(' ')
    listOfBooks = f.readlines()

bookSizeList = [int(bookSize.split(' ').pop(0)) for bookSize in listOfBooks]

shelfSum = 0
sumCount = 0
for shelf in shelfList:
    sumCount+=1
    if((shelfSum + int(shelf)) > sum(bookSizeList)):
        print(shelfSum)
    else:
        shelfSum+=int(shelf)
