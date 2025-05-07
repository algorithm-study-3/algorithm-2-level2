T = int(input())

for _ in range(T):
    n = int(input())
    open = []

    for i in range(1, n + 1):
        s = i
        mul = 1
        while s <= n:
            if s in open:
                open.remove(s)
            else:
                open.append(s)
            mul += 1
            s = i * mul

    print(len(open))