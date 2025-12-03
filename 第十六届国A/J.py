n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(k):

    x = b[0] - a[k]
    for i in range(n):
        if a[(i + k) % n] + x != b[i]:
            return False
    return True

ans = -1
for k in range(n):
    if check(k):
        ans = k
        break

print(ans)
