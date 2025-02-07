N = int(input())
nums = list(map(int,input().split()))

max_array = [0]*N
max_array[0] = nums[0]
for i in range(1,N):
    max_array[i] = max(max_array[i-1] + nums[i], nums[i])

print(max(max_array))