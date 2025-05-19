T = int(input())

for _ in range(T):
    words = input().split()
    ans = []
    
    for w in words:
        ans.append(w[::-1])

    print(' '.join(ans))