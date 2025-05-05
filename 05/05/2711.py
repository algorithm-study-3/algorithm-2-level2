T = int(input())

for _ in range(T):
    l, s = input().split()
    print(s[:int(l) - 1] + s[int(l):])