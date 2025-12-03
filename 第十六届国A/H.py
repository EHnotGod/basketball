
n = int(input())
lis = []
for i in range(n):
    s = input()
    u, v = s.split()
    lis.append([int(u), list(v.split("/"))])

m = int(input())
def pan(eee, q):
    if "**" in eee:
        idx = eee.index("**")
        qian = eee[:idx]
        hou = eee[idx+1:]
        if len(qian) + len(hou) > len(q):
            return False
        for i in range(len(qian)):
            if qian[i] != q[i]:
                return False
        for i in range(1, len(hou) + 1):
            if hou[-i] != q[-i]:
                return False
        return True
    else:
        if len(eee) != len(q):
            return False
        n = len(eee)
        for i in range(n):
            if eee[i] != q[i] and eee[i] != "*":
                return False
        return True
for i in range(m):
    s = input()
    lin = list(s.split("/"))
    ma = 0
    for j in range(n):
        if pan(lis[j][1], lin):
            ma = max(ma, lis[j][0])
    if ma == 0:
        print("SAFE")
    else:
        print("ALERT:", ma)

