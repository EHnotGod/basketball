n = int(input())
a = list(map(int, input().split()))
ans = 0

pre = a[1] - a[0]

def check(cnt, x, zuo, you):
    tmppre = you - x
    for i in range(cnt):
        tmppre = (tmppre + 1) // 2
        x -= tmppre
    if x >= zuo:
        return True
    else:
        return False

for i in range(n - 2):
    l = a[i + 1]
    you = a[i + 2] - a[i + 1]
    if you > 2 * pre:

        cnt = 0
        while you > 2 * pre:
            pre *= 2
            you -= pre
            l += pre
            cnt += 1
        ll = a[i + 1] + (a[i + 2] - a[i + 1] + 2) // 3
        rr = l
        while ll < rr:
            zhong = (ll + rr) // 2
            if check(cnt, zhong, a[i + 1], a[i + 2]):
                rr = zhong
            else:
                ll = zhong + 1

        idx = ll
        pre = a[i + 2] - idx
        ans += cnt
    else:
        pre = a[i + 2] - a[i + 1]
print(ans)
