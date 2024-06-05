def solution(routes:list):
    ans=1
    routes.sort()
    camera=routes[0][1]
    for i in range(1,len(routes)):
        st,ed=routes[i]
        if st>camera:
            ans+=1
            camera=ed
        else:
            camera=min(camera,ed)
    return ans