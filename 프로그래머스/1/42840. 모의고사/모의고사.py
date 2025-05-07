def solution(answers):
    N = len(answers)
    first = [1,2,3,4,5]*(N//5)+[1,2,3,4,5][:N%5]
    second = [2,1,2,3,2,4,2,5]*(N//8)+[2,1,2,3,2,4,2,5][:N%8]
    third = [3,3,1,1,2,2,4,4,5,5]*(N//10)+[3,3,1,1,2,2,4,4,5,5][:N%10]
    scores = [sum([a == b for a, b in zip(answers,first)]),
              sum([a == b for a, b in zip(answers,second)]),
              sum([a == b for a, b in zip(answers,third)])
             ]
    max_score = max(scores)
    return [idx for idx,s in enumerate(scores,start=1) if s == max_score]