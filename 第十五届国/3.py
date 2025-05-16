fus = "~!@#$%^&*()_"
fu = set([i for i in fus])
da = set([chr(i) for i in range(ord('A'), ord('Z')+1)])
xiao = set([chr(i) for i in range(ord('a'), ord('z')+1)])
shu = set([str(i) for i in range(10)])
t = int(input())
for i in range(t):
    s = input()
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    zhong = set()
    for i in s:
        if i in fu:
            flag1 = 1
            zhong.add(i)
        elif i in da:
            flag2 = 1
        elif i in xiao:
            flag3 = 1
        elif i in shu:
            flag4 = 1
        else:
            flag5 = 1
    if flag5:
        print(0)
        continue

    he = [flag1, flag2, flag3, flag4]
    su = sum(he)
    if len(s) >= 12 and (su == 4 or (flag1 == 1 and su >= 3 and len(zhong) >= 3)):
        print(3)
        continue
    if len(s) >= 8 and su >= 2:
        print(2)
        continue
    if len(s) >= 6:
        print(1)
        continue
    print(0)