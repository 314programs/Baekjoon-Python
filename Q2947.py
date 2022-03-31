#Continue the C++
input_list = list(map(int, input().split()))
while input_list != [1,2,3,4,5]:
    for i in range(4):
        if input_list[i] > input_list[i+1]:
            temp_1 = input_list[i]
            temp_2 = input_list[i+1]

            input_list[i] = temp_2
            input_list[i+1] = temp_1
            print(' '.join(map(str, input_list)))
