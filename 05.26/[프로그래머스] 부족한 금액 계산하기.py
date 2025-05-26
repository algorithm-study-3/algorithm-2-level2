def solution(price, money, count):
    need_price = 0
    for i in range(count):
        need_price += (i + 1) * price
    
    if(need_price > money):
        return need_price - money
    
    return 0