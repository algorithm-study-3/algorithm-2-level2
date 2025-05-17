X = int(input())

while X < 10000:
    X = int(X) + 1
    X = str(X)
    y1, y2 = int(X[:2]), int(X[2:])

    if pow(y1 + y2, 2) == int(X):
        print(X)
        exit(0)
    X = int(X)

print(-1)