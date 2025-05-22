def get_divisor(n):
    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if(i > right): break
        if(len(get_divisor(i)) % 2 == 0):
            answer += i
        else:
            answer -= i

    return answer