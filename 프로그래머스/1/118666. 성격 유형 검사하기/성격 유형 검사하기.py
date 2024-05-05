def choice(li):
    if dict[li[0]]>=dict[li[1]]:
        return li[0]
    else:
        return li[1]
def solution(survey, choices):
    global dict
    dict = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    question = len(survey)
    for i in range(question):
        first = survey[i][0]
        second = survey[i][1]
        if choices[i]<4:
            dict[first]+=(4-choices[i])
        elif choices[i]>4:
            dict[second]+=(choices[i]-4)
    char = [["R","T"],["C","F"],["J","M"],["A","N"]]
    MBTI = ""

    for c in char:
        MBTI+=choice(c)
    
    return MBTI