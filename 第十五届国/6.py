t = int(input())
lis = []
id = 0
for _ in range(t):
    s = input()
    if len(lis) == 0:
        if s[0] == "i":
            for i in s[8:len(s) - 1]:
                lis.append(i)
                id = len(s) - 9
    else:
        if s[0] == "i":
            for i in s[8:len(s) - 1]:
                lis.insert(id, i)
                id += 1
        elif s[0] == "d":
            shu = int(s[1:len(s) - 1])
            if s[-1] == "h":
                for i in range(max(id - shu, 0), id):
                    del lis[max(id - shu, 0)]
                id -= id - max(id - shu, 0)
            else:
                for i in range(id, min(id + shu, len(lis))):
                    del lis[id]
        else:
            shu = int(s[:len(s) - 1])
            if s[-1] == "h":
                id = max(id - shu, 0)
            else:
                id = min(id + shu, len(lis))

for i in lis:
    print(i, end="")






