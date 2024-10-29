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
    return 1 if not stk else 0