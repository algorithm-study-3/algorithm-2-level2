# 풀이 1
N = int(input())
names = []

for _ in range(N):
    names.append(input())

sorted_names = sorted(names)

for n in sorted_names:
    if len(n) == 3:
        print(n)
        exit(0)

# 풀이 2
N = int(input())
names = []

for _ in range(N):
    names.append(input())

three_names = [x for x in sorted(names) if len(x) == 3]

print(three_names[0])