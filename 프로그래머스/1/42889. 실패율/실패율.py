def solution(N, stages):
    answer = []
    stage = dict()
    for i in range(1,502):
        stage[i] = 0
    
    for s in stages:
        stage[s]+=1

    challenge = []
    ppl = len(stages)
    
    for k,v in stage.items():
        if k <= N:
            if ppl!=0:
                challenge.append([k,v/ppl])
                ppl-=v
            else:
                challenge.append([k,0])
                


    challenge.sort(key=lambda x: (-x[1],x[0]))
    answer = [c[0] for c in challenge]


    return answer