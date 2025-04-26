L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

ans = []

if A % C != 0:
    ans.append(A // C + 1)
else:
    ans.append(A // C)

if B % D != 0:
    ans.append(B // D + 1)
else:
    ans.append(B // D)

print(L - max(ans))