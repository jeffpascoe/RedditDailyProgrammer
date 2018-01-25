import inflect
p = inflect.engine()

with open('/Users/JeffPascoe/Documents/Github Projects/RedditDailyProgrammer/Challenge321/input.txt') as f:
    timeList = f.readlines()

timeListMapping = [map(int, time.split(':')) for time in timeList]

for time in timeListMapping:
    time.append('am')
    if(time[0]>12): time[0] -= 12; time[2]='pm'
    elif(time[0] == 00): time[0] = 12
    time[0] = p.number_to_words(time[0]); time[1] = p.number_to_words(time[1]);
    if(time[1]=='zero'): time[1]=''
    print('It''s {} {} {}'.format(time[0], time[1], time[2]))
