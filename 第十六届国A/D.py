import copy

n, mi, ma = map(int, input().split())
lis = []
for i in range(n):
    s = input()
    if len(s) <= mi:
        lis.append([s])
    else:
        lin = []
        for j in range(len(s) - mi + 1):
            lin.append(s[j: j + mi])
        lis.append(copy.copy(lin))
q = input()
q_lis = []
if len(q) <= mi:
    q_lis.append(q)
else:
    for j in range(len(q) - mi + 1):
        q_lis.append(q[j: j + mi])
ans = 0
for i in lis:
    for j in q_lis:
        if j in i:
            ans += 1
            break
print(ans)