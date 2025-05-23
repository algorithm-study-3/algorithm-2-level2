def solution(s):
    sorted_s = sorted(s)
    sorted_s.reverse() # reverse는 return 값이 없고, 원본을 바꾸기만 함(몰랐던 거)
    answer = ''.join(sorted_s)
    return answer