def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def solution(n: int, computers: list):
    global parents
    parents = [i for i in range(n)]
    
    for i in range(n-1):
        for j in range(i+1,n):
            if computers[i][j] == 1:
                union(i, j)
    
    for i in range(n):
        find(i)


    return len(set(parents))

