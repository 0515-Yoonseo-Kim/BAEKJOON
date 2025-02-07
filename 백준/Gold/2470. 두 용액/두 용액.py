import heapq

N = int(input())
sol_li = sorted(list(map(int,input().split())))

left,right = 0,N-1
priority_queue = []
while left<right:
    total = sol_li[left] + sol_li[right]
    heapq.heappush(priority_queue,(abs(total),left,right))
    if total>0:
        right-=1
    elif total<0:
        left+=1
    else:
        break

m,l,r = heapq.heappop(priority_queue)
print(sol_li[l],sol_li[r])