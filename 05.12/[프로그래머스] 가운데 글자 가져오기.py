def solution(s):
    answer = ''
    s_len = len(s)
    if( s_len % 2 == 0):
        middle = s_len // 2
        answer = s[middle - 1: middle+1]
    else:
        middle = s_len // 2
        answer = s[middle]
    return answer