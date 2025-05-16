import sys
input=sys.stdin.readline
print=sys.stdout.write

n, m = map(int, input().split())
lis = list(map(int, input().split()))
p = list(map(float, input().split()))
qian = [0]
he = 0
for i in range(m):
    he += p[i]
    qian.append(he)
dp = [[0 for j in range(2 ** n)] for i in range(m + 1)]

zhiling = [[] for j in range(2 ** n)]

for k in range(2 ** n):
    bi = list(map(int, bin(k)[2:].zfill(n).strip()))
    lin = [0] * n
    for j in range(n):
        if bi[n - 1 - j] == 0:
            lin[j] = k | (1 << j)
    for j in range(n):
        if lin[j] != 0:
            zhiling[k].append((j, lin[j]))

for i in range(1, m + 1):
    for k in range(2 ** n):
        dp[i][k] = max(dp[i][k], dp[i - 1][k])
        for each in zhiling[k]:
            j, idx = each
            dp[i][idx] = max(dp[i][idx], qian[i] - qian[i - lis[j]] + dp[max(0, i - lis[j])][k])

print("{:.2f}".format(qian[m] - max(dp[m])))
