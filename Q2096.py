#My first sliding window
Height = int(input())
List = list(map(int, input().split()))
if Height == 1:
    print(max(List), min(List))
else:
    DP_min = List
    DP_max = List
    for i in range(Height-1):
      #I hate DP so much
      #I managed to make a sequence structure but my code was incorrect
        a,b,c = map(int, input().split())
        DP_min = [a + min(DP_min[0], DP_min[1]), b + min(DP_min[0], DP_min[1], DP_min[2]), c + min(DP_min[1], DP_min[2])]
        DP_max = [a + max(DP_max[0], DP_max[1]), b + max(DP_max[0], DP_max[1], DP_max[2]), c + max(DP_max[1], DP_max[2])]
    print(max(DP_max), min(DP_min))
