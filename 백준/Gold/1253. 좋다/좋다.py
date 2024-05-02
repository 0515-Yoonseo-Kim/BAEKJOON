N = int(input())
num_list = list(map(int,input().split()))
num_list.sort()

cnt = 0


for idx,num in enumerate(num_list):
    
    now = num_list[:idx]+num_list[idx+1:]
    st,ed = 0, len(now)-1

    while st<ed:
        interval_sum = now[st]+now[ed]
        if interval_sum < num:
            st+=1
        elif interval_sum > num:
            ed-=1
        else:
            cnt+=1
            break


print(cnt)
