import math
from typing import List

N = int(input())
result = list(map(int,input().split()))
max_k = int(math.log2(N)) # max_k : 2**k<=N을 만족하는 k의 최댓값 

# 카드 복원 함수
def restore_card(li:List[int],k:int,goal:int)-> List[int]:
    if k > goal:
        li = li[2**goal:]+li[:2**goal]
        return li
    dummy = li[:2**k] # 섞는 카드 더미
    remains = li[2**k:] # 안섞는 카드 더미
    new_dummy = dummy[len(dummy)//2:] + dummy[:len(dummy)//2]
    return restore_card(new_dummy+remains,k+1,goal) # 재귀


check = False # 이중 루프 탈출용
original = [i for i in range(1,N+1)]
for k1 in range(1,max_k+1):
    for k2 in range(1,max_k+1):
        ans = restore_card(restore_card(result,1,k2),1,k1) # 두 번 섞어서
        if ans == original:
            print(k1,k2)
            check=True
            break ## 정해진 조합이 나오면 탈출
    if check:
        break