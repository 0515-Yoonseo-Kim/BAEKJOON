import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
partial_arr = [[0 for _ in range(M)] for _ in range(N)]
max_value = -10000
for i in range(N):
    for j in range(M):
        partial_arr[i][j] = arr[i][j]
        if i >= 1:
            partial_arr[i][j] += partial_arr[i-1][j]
        if j >= 1:
            partial_arr[i][j] += partial_arr[i][j-1]
        if i >= 1 and j >= 1:
            partial_arr[i][j] -= partial_arr[i-1][j-1]

for sr in range(N):
    for sc in range(M):
        for fr in range(sr,N):
            for fc in range(sc,M):
                temp = partial_arr[fr][fc]
                if sr >=1:
                    temp -= partial_arr[sr-1][fc]
                if sc >=1:
                    temp -= partial_arr[fr][sc-1]
                if sr>=1 and sc>=1:
                    temp += partial_arr[sr-1][sc-1]
                max_value = max(max_value,temp)
        
print(max_value)