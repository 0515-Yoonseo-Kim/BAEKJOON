def solution(targets):
    targets.sort(key = lambda x: x[1])
    camera = targets[0][1]-0.5
    cnt = 1
    for target in targets:
        st,ed = target
        if st>camera:
            cnt += 1
            camera = ed-0.5
    return cnt