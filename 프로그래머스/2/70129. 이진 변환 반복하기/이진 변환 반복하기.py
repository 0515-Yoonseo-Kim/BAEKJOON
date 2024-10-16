def binary_convert(string: str):
    zero_count = string.count("0")
    string = string.replace("0", "")
    len_str = len(string)
    bin_str = bin(len_str)[2:]
    return bin_str, zero_count

def solution(s):
    stk = [0,0]
    while s!="1":
        s, removed_zero = binary_convert(s)
        stk[0] += 1
        stk[1] += removed_zero
    return stk