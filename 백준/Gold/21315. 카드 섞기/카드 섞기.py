import math,sys
from typing import List

N = int(input())
result = list(map(int,input().split()))
max_k = int(math.log2(N))

def mix_card(li:List[int],k:int,goal:int):
    if k > goal:
        li = li[2**goal:]+li[:2**goal]
        return li
    dummy = li[:2**k]
    remains = li[2**k:]
    new_dummy = dummy[len(dummy)//2:] + dummy[:len(dummy)//2]
    return mix_card(new_dummy+remains,k+1,goal)

ans_list = []
check = False
for k1 in range(1,max_k+1):
    for k2 in range(1,max_k+1):
        ans = mix_card(mix_card(result,1,k2),1,k1)
        if ans == [i for i in range(1,N+1)]:
            ans_list+=[k1,k2]
            check=True
            break
    if check:
        break

print(*ans_list)