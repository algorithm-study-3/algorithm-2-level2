from collections import deque

def bfs(n, m, dx, dy, maps):
    q = deque()
    q.append((0, 0))
    
    while q:
        cx, cy = q.popleft()
        
        if cx == n - 1 and cy == m - 1:
            return maps[cx][cy]
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = maps[cx][cy] + 1
                
    return -1

def solution(maps):   
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n, m = len(maps), len(maps[0])
    
    if bfs(n, m, dx, dy, maps) == -1:
        return -1
    else:
        return maps[n - 1][m - 1]