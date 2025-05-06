import math

N = int(input())
s = math.ceil(N / 7)
next = s
ans = 0

while True:
    for _ in range(7):
        ans += next
        next -= 1
        if next < 1:
            next = 0
    if ans >= N:
        print(s)
        exit(0)
    else:
        s += 1
        next = s
        ans = 0