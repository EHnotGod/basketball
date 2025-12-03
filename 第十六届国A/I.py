from collections import defaultdict
import math

n = int(input())
n += 1
C = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
d = defaultdict(int)
for i in range(1, n + 1):
    C[i][0] = 1
    for j in range(1, i + 1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]
        if 2 <= C[i][j] <= n - 1:
            d[C[i][j]] += 1

d2 = defaultdict(int)
for i in d:
    d2[d[i]] += 1

ans = []
for i in d2:
    ans.append([i, d2[i]])
ans.sort(key=lambda x: x[0])

for i in ans:
    print(*i)
