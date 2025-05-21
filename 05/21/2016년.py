def solution(a, b):
    ans = 0
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    if a == 1:
        ans += b
    else:
        for i in range(0, a - 1):
            ans += days[i]
        ans += b
        
    idx = ans % 7 - 1
    if idx == -1:
        idx = 6
    
    return day[ans % 7 - 1]