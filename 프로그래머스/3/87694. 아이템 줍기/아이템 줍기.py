from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):

    arr = [[-1 for _ in range(102)] for _ in range(102)]
    for rect in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2,rect)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if x1<x<x2 and y1<y<y2:
                    arr[x][y]=0
                elif arr[x][y]!=0:
                    arr[x][y]=1

    def bfs():
        queue = deque()
        visited = [[False for _ in range(102)] for _ in range(102)] 
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        stx,sty=characterX*2,characterY*2
        visited[stx][sty] = True
        queue.append([stx,sty,0])
        while queue:
            x,y,dist = queue.popleft()
            
            if x==2*itemX and y==2*itemY:
                return dist//2
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx,ny,dist+1])
                    visited[nx][ny]=True

    return bfs()


