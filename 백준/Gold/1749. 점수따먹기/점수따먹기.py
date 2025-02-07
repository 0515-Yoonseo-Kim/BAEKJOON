import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_value = -float('inf')

for top in range(N):  
    temp = [0] * M
    
    for bottom in range(top, N):
        for col in range(M):
            temp[col] += arr[bottom][col]
        current_sum = 0
        local_max = -float('inf')
        
        for value in temp:
            current_sum += value
            local_max = max(local_max, current_sum)
            
            if current_sum < 0:
                current_sum = 0
        
        max_value = max(max_value, local_max)

print(max_value)
