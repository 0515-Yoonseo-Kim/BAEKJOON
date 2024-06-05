def solution(routes):
    routes.sort()
    cam = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        if routes[i][0] > cam:
            answer += 1
            cam = routes[i][1]
        else:
            cam = min(cam, routes[i][1])
    return answer