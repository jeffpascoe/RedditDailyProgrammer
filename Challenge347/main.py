from sets import Set

with open('/Users/JeffPascoe/Documents/Github Projects/RedditDailyProgrammer/Challenge347/input.txt') as f:
	timeIntervals = f.readlines()

strings = []
for interval in timeIntervals:
	temp = interval.strip('\n')
	strings.append(temp.split(' '))

sumList = list(map((lambda x: range(int(x[0]),int(x[1]))), strings))
flat_list = len(Set([item for sublist in sumList for item in sublist]))

print(flat_list)
