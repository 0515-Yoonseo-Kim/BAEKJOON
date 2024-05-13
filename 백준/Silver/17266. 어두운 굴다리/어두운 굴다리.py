from math import ceil
N = int(input())
M = int(input())
road = [0]*N
light = list(map(int,input().split()))
diff = [ceil((light[i+1] - light[i])/2) for i in range(M-1)]
max_diff = 0
if diff:
    max_diff = max(diff)


max_height = max(light[0],N-light[-1],max_diff)

print(max_height)

