N = int(input())
m = input()
K = int(input())

if m == "annyong":
    if K % 2 == 1:
        print(K)
        exit(0)
    else:
        if K - 1 > 0:
            print(K - 1)
            exit(0)
        else:
            print(K + 1)
            exit(0)

else:
    if K % 2 == 0:
        print(K)
        exit(0)
    else:
        if K - 1 > 0:
            print(K - 1)
            exit(0)
        else:
            print(K + 1)
            exit(0)