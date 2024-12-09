N, M = map(int,input().split())
num_li = sorted(list(map(int,input().split())))
ans_li = []
def bt(li,max_idx):
    if len(li) == M:
        ans_li.append(li)
        return
    
    for idx in range(max_idx+1,N):
        bt(li+[num_li[idx]],idx)


for i in range(N-M+1):
    bt([num_li[i]],i)

for ans in ans_li:
    print(*ans)