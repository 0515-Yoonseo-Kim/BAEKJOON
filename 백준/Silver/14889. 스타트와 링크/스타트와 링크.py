N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [False]*N
result = 20*20*101


def abs(num):
    if num < 0:
        return -num
    else:
        return num


def divide(length,idx):
    global result
    if length == N//2:
        start,link = 0,0
        for i in range(N):
            for j in range(i,N):
                if visited[i] and visited[j]:
                    start+=arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j] + arr[j][i]
        result = min(result, abs(start-link))
        return
    
    else:
        for i in range(idx,N):
            if not visited[i]:
                visited[i] = True
                divide(length+1,i+1)
                visited[i] = False
    
    

divide(0,0)
print(result)