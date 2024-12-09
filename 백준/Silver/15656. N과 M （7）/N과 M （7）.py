N,M=map(int,input().split())
num_li=sorted(list(map(int,input().split())))
ans_li = []
def bt(li):
    if len(li) == M:
        ans_li.append(li)
        return
    
    for num in num_li:
        bt(li+[num])

for num in num_li:
    bt([num])
for ans in ans_li:
    print(*ans)