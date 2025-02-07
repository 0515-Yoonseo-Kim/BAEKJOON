import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_value = -float('inf')  # 최댓값 초기화

# top부터 bottom까지의 행들을 고정하여 처리
for top in range(N):  
    temp = [0] * M  # 각 열에 대한 부분 합을 저장할 배열
    
    # bottom 행을 고정하여, top 행부터 bottom 행까지의 합을 구함
    for bottom in range(top, N):
        # 각 열에 대해 해당하는 부분 합을 계산
        for col in range(M):
            temp[col] += arr[bottom][col]
        
        # temp 배열에 대해 Kadane's Algorithm을 적용하여 최대 부분합을 구함
        current_sum = 0
        local_max = -float('inf')
        
        for value in temp:
            current_sum += value
            local_max = max(local_max, current_sum)
            
            if current_sum < 0:
                current_sum = 0
        
        # 최댓값 갱신
        max_value = max(max_value, local_max)

# 출력
print(max_value)
