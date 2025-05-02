N = int(input())

for _ in range(N):
    f = input()
    if f[len(f) // 2 - 1] == f[len(f) // 2]:
        print("Do-it")
    else:
        print("Do-it-Not")