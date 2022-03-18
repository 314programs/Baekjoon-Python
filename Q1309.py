#I should always write sequences when doing DP...
Rows = int(input())
Divider = 9901

if Rows == 1:
    print(3)
else:
    DP = [0 for i in range(Rows + 1)]

    DP[0] = 1
    DP[1] = 3

    for r in range(2, Rows + 1):
        DP[r] = (DP[r-2] + DP[r-1] * 2) % Divider

    print(DP[Rows]%Divider)
