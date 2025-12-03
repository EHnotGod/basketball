import sys
sys.setrecursionlimit(int(1e5))
n, k = map(int, input().split())
e = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    e[u].append([v, w])
    e[v].append([u, w])
ma = 0
def zou(x, shu, zhi):
    vis[x] = 1
    if shu == k:
        global ma
        ma += zhi
        return
    for i, j in e[x]:
        if vis[i] == 0:
            zou(i, shu + 1, zhi + j)
for i in range(1, n + 1):
    vis = [0] * (n + 1)
    zou(i, 0, 0)
print(ma)