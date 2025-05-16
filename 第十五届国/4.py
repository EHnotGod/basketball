n, m, l = map(int, input().split())
t = list(map(int, input().split()))
q = [m for i in range(10000)]
ans = 0
for i in range(l):
    ti = t[i] // n
    if q[ti] > 0:
        ans += 1
        q[ti] -= 1
print(ans)