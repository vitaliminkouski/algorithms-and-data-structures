
with open('in.txt', 'r') as f:
    pD = int(f.readline().strip())
    pI = int(f.readline().strip())
    pR = int(f.readline().strip())
    A = f.readline().strip()
    B = f.readline().strip()

n = len(A)
m = len(B)


dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 1] + pI

for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + pD

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost_del = dp[i - 1][j] + pD
        cost_ins = dp[i][j - 1] + pI
        cost_rep = dp[i - 1][j - 1] + (0 if A[i - 1] == B[j - 1] else pR)

        dp[i][j] = min(cost_del, cost_ins, cost_rep)

with open('out.txt', 'w') as f:
    f.write(str(dp[n][m]) + '\n')
