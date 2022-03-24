#for fun?
list_len, repeat = map(int, input().split())
num_list = list(map(int, input().split(',')))

for i in range(repeat):
    temp = [0 for v in range(list_len-1)]
    for x in range(list_len-1):
        temp[x] = num_list[x + 1] - num_list[x]
    
    num_list = temp
    list_len = len(num_list) 

print(','.join(map(str, num_list)))
