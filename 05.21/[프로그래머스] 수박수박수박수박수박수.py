def solution(n):
    pattern =  ['수', '박']
    answer = ''
    for i in range(n):
        answer += pattern[i % 2]
    return answer