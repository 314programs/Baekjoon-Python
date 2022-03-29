#Learning C++... slowing down on python now
cases = int(input())
for case in range(cases):
    delete_index, word = map(str, input().split())
    print(word[:int(delete_index)-1] + word[int(delete_index):])
