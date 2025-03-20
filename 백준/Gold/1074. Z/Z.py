N,r,c = map(int,input().split())
cnt = 0
while N > 0:
    prefix = 2**(N-1) # 4
    temp = 0
    if r >= prefix:
        r -= prefix
        temp += 2
    if c >= prefix:
        c -= prefix
        temp += 1
    cnt += 4**(N-1)*temp
    N -= 1
print(cnt)