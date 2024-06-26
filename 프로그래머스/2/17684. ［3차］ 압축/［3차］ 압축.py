def solution(msg):
    lzw_dict = {}
    for i  in range(1,27):
        lzw_dict[i]=chr(i+64)

    str_stk = ""
    next_idx = 27
    ans = []
    for idx, s in enumerate(msg):
        str_stk += s
        if str_stk in lzw_dict.values():
            continue
        else:
            lzw_dict[next_idx] = str_stk
            next_idx +=1
            ans.append(str_stk[:-1])
            str_stk = str_stk[-1]
    if str_stk:
        ans.append(str_stk)
    
    ans_dict = {v:k for k,v in lzw_dict.items()}
    return [ans_dict[a] for a in ans]