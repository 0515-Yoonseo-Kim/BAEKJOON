def solution(triangle):
    for idx,tri in enumerate(triangle[1:],start=1):
        for j in range(len(tri)):
            if j==0:
                triangle[idx][j]+=triangle[idx-1][j]
                pass
            elif j==len(tri)-1:
                triangle[idx][j]+=triangle[idx-1][j-1]
            else:
                triangle[idx][j]+=max(triangle[idx-1][j-1],triangle[idx-1][j])
            
    return max(triangle[-1])