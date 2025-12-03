import sys
sys.setrecursionlimit(int(1e5))
n = int(input())
e = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
ma = 0
def zou(x, shu):
    vis[x] = 1
    if shu % 2 == 0:
        global ma
        ma = max(ma, shu)
    for i in e[x]:
        if vis[i] == 0:
            zou(i, shu + 1)
for i in range(1, n + 1):
    vis = [0] * (n + 1)
    zou(i, 0)
print(ma)