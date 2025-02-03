N, S = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
def bt(idx,total):
    global cnt
    if idx == N:
        return 
    total += nums[idx]
    if total == S:
        cnt += 1
    bt(idx + 1,total)
    bt(idx+1, total-nums[idx])

bt(0,0)
print(cnt)