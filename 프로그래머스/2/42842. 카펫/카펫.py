def solution(brown, yellow):
    # brown = 2*(x+y-2) / yellow = (x-2)*(y-2)
    for x in range(3,2500):
        for y in range(3,x+1):
            b, yel = 2*(x+y-2), (x-2)*(y-2)
            if b == brown and yel == yellow:
                return x,y