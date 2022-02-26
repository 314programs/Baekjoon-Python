#In a hotel
hour, minute = map(int, input().split())
added_minute = int(input())

hour += (minute + added_minute)//60
minute = (minute + added_minute)%60

print(hour%24, minute)
