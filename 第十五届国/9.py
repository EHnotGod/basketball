import sys
input = sys.stdin.readline

x, y = map(int, input().split())

mod = int(1e9 + 7)

def pan(x):
    ll = list(str(x).strip())
    if "2" in ll or "4" in ll:
        return 0
    return 1

ans = 0
s = list(map(int, str(x).strip()))
chang = len(s)
yu = [[[0 for i in range(2)] for j in range(2024)] for _ in range(chang)]
for i in range(chang):
    si = s[i]
    if i == 0:
        for j in range(si + 1):
            if j == 2 or j == 4:
                continue
            idx = 10 ** (chang - i - 1) * j % 2024
            if j == si:
                yu[i][idx][1] += 1
            else:
                yu[i][idx][0] += 1
    else:
        for j in range(si + 1):
            if j == 2 or j == 4:
                continue
            idx = 10 ** (chang - i - 1) * j % 2024
            for k in range(2024):
                if j == si:
                    yu[i][(idx + k) % 2024][1] += yu[i - 1][k][1]
                else:
                    yu[i][(idx + k) % 2024][0] += yu[i - 1][k][1]
        for j in range(10):
            if j == 2 or j == 4:
                continue
            idx = 10 ** (chang - i - 1) * j % 2024
            for k in range(2024):
                yu[i][(idx + k) % 2024][0] += yu[i - 1][k][0]

yu = [(yu[-1][i][0] + yu[-1][i][1]) % mod for i in range(2024)]

yu[0] -= 1


for i in range(2024):
    for j in range(i, 2024):
        k = (4048 + y - i - j) % 2024
        if k < j:
            continue
        if (i + j + k) % 2024 != y:
            continue
        if i == j and k > j:
            ans += yu[i] * (yu[i] - 1) * yu[k] // 2
            ans %= mod
        elif i == j and k == j:
            ans += yu[i] * (yu[i] - 1) * (yu[i] - 2) // 6
            ans %= mod
        elif i != j and k == j:
            ans += yu[j] * (yu[j] - 1) * yu[i] // 2
            ans %= mod
        else:
            ans += yu[i] * yu[j] * yu[k]
            ans %= mod
print(ans)