N = int(input())
ans = 0

for _ in range(N):
    s = []
    word = input()

    for w in word:
        if len(s) == 0:
            s.append(w)
        elif s[-1] == w:
            s.pop()
        else:
            s.append(w)

    if len(s) == 0:
        ans += 1

print(ans)