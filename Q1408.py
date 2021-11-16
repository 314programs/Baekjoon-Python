Start = list(map(int, input().split(':')))
End = list(map(int, input().split(':')))

Sec = 0
Min = 0
Hour = 0

if End[2] < Start[2]:
    End[2] += 60
    End[1] -= 1
if End[1] < Start[1]:
    End[1] += 60
    End[0] -= 1
if End[0] < Start[0]:
    End[0] += 24
    
Sec += (End[2]-Start[2])
Min += (End[1]-Start[1])
Hour += (End[0]-Start[0])

def Check(num):
    if len(str(num)) == 1:
        num = '0' + str(num)
    return num
        
Sec = Check(Sec)
Min = Check(Min)
Hour = Check(Hour)

print(str(Hour)+':'+str(Min)+':'+str(Sec))

