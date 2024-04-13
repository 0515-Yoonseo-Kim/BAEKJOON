N = int(input())
local = list(map(int,input().split()))
budget = int(input())



def binary_search(budget):
    low = 0
    high = max(local)
    if sum(local)<=budget:
        return max(local)
    
    else:
        while low<high:
            cnt = 0
            mid = (low+high)//2
            temp = 0
            for l in local:
                if l<mid:
                    temp+=l
                else:
                    temp+=mid
                    cnt+=1
            if budget-cnt<temp<=budget:
                return mid
            

            if temp < budget:
                low = mid
                continue
            elif temp > budget:
                high = mid                
                continue
            

print(binary_search(budget))

