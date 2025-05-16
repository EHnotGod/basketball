n = int(input())
lis = list(map(int, input().split()))
ans = 0
se = set()
r = 0
l = 0
for i in range(n - 1, -1, -1):
    if lis[i] not in se:
        se.add(lis[i])
    else:
        ans = n - 1 - i
        r = i + 1
        break
if ans == 0:
    print(n)
else:
    while l < n and r < n:
        while r < n and lis[l] in se:
            se.remove(lis[r])
            r += 1
        if lis[l] in se:
            break
        se.add(lis[l])
        ans = max(ans, len(se))
        l += 1
    se = set()
    ans2 = 0
    for i in range(n):
        if lis[i] not in se:
            se.add(lis[i])
        else:
            ans2 = i
            break
    print(max(ans, ans2))