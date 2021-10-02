#Get input and set up list for members and counting
Grade, NumPeople = map(int, input().split())
BlueMember = []
BlueCount = []
WhiteMember = []
WhiteCount = []

while True:
  grade, name = map(str, input().split())
  namelen = len(name)
  
#We count grades using count list so that people joining has a limit
  if grade == '0' and name == '0':
    break
  elif int(grade)%2 == 0 and int(grade) <= Grade and WhiteCount.count(int(grade)) < NumPeople:
    WhiteMember.append([int(grade), name, namelen])
    WhiteCount.append(int(grade))
  elif int(grade)%2 != 0 and int(grade) <= Grade and BlueCount.count(int(grade)) < NumPeople:
    BlueMember.append([int(grade), name, namelen])
    BlueCount.append(int(grade))

#Sort on grade first, than length of the name and finally the alphabetical order of the name
BlueMember.sort(key = lambda x: (x[0], x[2], x[1]))
WhiteMember.sort(key = lambda x: (x[0], x[2], x[1]))

#Print
for item in BlueMember:
  print(str(item[0]) + ' ' + item[1])

for item in WhiteMember:
  print(str(item[0]) + ' ' + item[1])
