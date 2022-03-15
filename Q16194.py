#DP practice without looking
card_pack_num = int(input())
cards = list(map(int, input().split()))

DP = [float('inf') for v in range(card_pack_num+1)]
DP[0] = 0

for i in range(1, card_pack_num+1):
    for j in range(1, card_pack_num+1):
        DP[i] = min(DP[i], DP[i-j] + cards[j-1])

print(DP[-1])
