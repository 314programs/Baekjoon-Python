#Get input and make a list
ScheduleNum = int(input())
Schedules = []
for i in range(ScheduleNum):
  Schedules.append(list(map(int, input().split())))

#Sort the list using lambda function, ending time needs to go first, then the starting time.
Schedules.sort(key=lambda x: (x[1],x[0]))
MeetingTime = [[0,0]]
Count = 0

#Check through each item in the sorted list and append it into MeetingTime
#Since this list is sorted, and MeetingTime gets updated, the values will not collide with each other.
for item in Schedules:
  if item[0] >= MeetingTime[-1][1]:
    MeetingTime.append(item)
    Count += 1

print(Count)
