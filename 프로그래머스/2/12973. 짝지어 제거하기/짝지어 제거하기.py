def solution(string):
    stk = []
    for s in string:
        if not stk:
            stk.append(s)
        else:
            if stk[-1]==s:
                stk.pop()
            else:
                stk.append(s)
    return int(not(stk))