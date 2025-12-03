import copy
import bisect
n = int(input())
lis = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if lis[i] > lis[i-1]:
        continue
    ling = len(str(lis[i - 1])) - len(str(lis[i]))
    se = set()
    se.add(lis[i])
    for j in range(ling):
        ans += 1
        se2 = set()
        for k in se:
            lin = list(str(k).strip())
            for kk in range(1, 1 + len(lin)):
                lin2 = copy.copy(lin)
                lin2.insert(kk, "0")
                se2.add(int("".join(lin2)))
        se = copy.copy(se2)
    if max(se) <= lis[i - 1]:
        ans += 1
        se2 = set()
        for k in se:
            lin = list(str(k).strip())
            for kk in range(1, 1 + len(lin)):
                lin2 = copy.copy(lin)
                lin2.insert(kk, "0")
                se2.add(int("".join(lin2)))
        se = copy.copy(se2)
    lis2 = list(se)
    lis2.sort()
    idx = bisect.bisect_right(lis2, lis[i - 1])
    lis[i] = lis2[idx]
# print(lis)
print(ans)
# 12
# 12 5 128 5 569 45 235 124 5876 458 489 125