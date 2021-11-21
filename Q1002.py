for i in range(int(input())):
    x1, y1, d1, x2, y2, d2 = map(int, input().split())
    
    #Calculate distance
    Distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    Inside = False

    if Distance + min(d1,d2) < max(d1,d2):
        Inside = True

    #Same circle
    if Distance == 0 and d1 == d2:
        print('-1')

    #Meets once outside or inside
    elif Distance == d1 + d2 or Distance + min(d1,d2) == max(d1,d2):
        print('1')

    #Does not meet
    elif Distance > d1 + d2 or Inside:
        print('0')

    #Meets twice   
    else:
        print('2')
    

