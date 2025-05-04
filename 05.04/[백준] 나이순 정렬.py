import sys
input = sys.stdin.readline

def main():
    n = int(input())
    members = []
    for _ in range(n):
        age, name = input().split()
        members.append((int(age), name))

    # 나이(age)만 기준으로 정렬 → 같은 나이면 기존 입력 순서 유지됨
    members.sort(key=lambda x: x[0])

    for age, name in members:
        print(age, name)

if __name__ == "__main__":
    main()