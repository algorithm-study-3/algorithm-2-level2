# num이 1일 때랑 반복 횟수가 500 이상일 때만 잘 처리해주면 됨
# while 문은 정확이 num이 1일 때 까지만 하면 되는 듯
# 그리고 실수 했던 점음 num을 2로 나눠야 하는데 num % 2 이렇게 해버렸음
# num / 2 로 고쳐가지고 이 문제를 해결 할 수 있었뜸

def solution(num):
    count = 0;
    
    if(num == 1): return 0

    while(num != 1):
        if (count >= 500): return -1
        
        if ((num % 2) == 0):
            count += 1
            num = num / 2
        elif ((num % 2) == 1):
            count += 1
            num = (num * 3) + 1
    
    return count