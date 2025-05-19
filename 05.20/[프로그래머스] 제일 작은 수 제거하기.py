def solution(arr):
    m = min(arr)
    arr.remove(m)
    if(len(arr) == 0):
        arr.append(-1)
        return arr
    return arr