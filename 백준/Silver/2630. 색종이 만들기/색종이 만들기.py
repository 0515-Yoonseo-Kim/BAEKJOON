# 1. 구역 전체가 같은 색깔이면 색깔에따라 1을 더해줘야 함.
# 2. 반씩 분할하면서 들어가기
import sys
from typing import List
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

white,blue = 0,0

# 하얀 색종이 개수, 파란 색종이 개수
def dfs(x: int,y: int,n: int) -> List[int]:
    global white, blue
    color = graph[x][y]
    half = n//2
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != graph[i][j]:
                dfs(x,y,half)
                dfs(x+half,y,half)
                dfs(x,y+half,half)
                dfs(x+half,y+half,half)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1
dfs(0,0,N)
print(white,blue)