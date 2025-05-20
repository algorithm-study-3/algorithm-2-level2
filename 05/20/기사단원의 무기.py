def solution(number, limit, power):
    answer = 0
    human = [i for i in range(1, number + 1)]
    
    for h in human:
        cnt = 0
        for i in range(1, int(h ** 0.5) + 1):
            if h % i == 0:
                cnt += 1
                if i != h // i:
                    cnt += 1
                
        if cnt > limit:
            answer += power
        else:
            answer += cnt
            
    return answer