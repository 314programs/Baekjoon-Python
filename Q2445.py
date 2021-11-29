num = int(input())
for i in range(1, num+1):
    word = i*'*' + ' '*(num-i)
    print(word + word[::-1])
for i in range(num-1, 0, -1):
    word = i*'*' + ' '*(num-i)
    print(word + word[::-1])
