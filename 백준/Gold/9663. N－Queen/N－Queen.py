N = int(input())
columns = {num for num in range(N)}

def bt(row,cols,diag1,diag2):
    if row == N:
        return 1
    cnt = 0
    for col in range(N):
        if (col in cols) or ((row-col) in diag1) or ((row+col) in diag2):
            continue
        cnt += bt(row+1,cols|{col},diag1|{row-col},diag2|{row+col})
    return cnt

print(bt(0,set(),set(),set()))