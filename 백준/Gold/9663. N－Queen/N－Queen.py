N = int(input())
columns = {num for num in range(N)}

def bt(row,cols,diag1,diag2):
    if row == N:
        return 1
    
    cnt = 0
    for col in range(N):
        if (col in cols) or ((row-col) in diag1) or ((row+col) in diag2):
            continue

        cols.add(col)
        diag1.add(row-col)
        diag2.add(row+col)

        cnt += bt(row+1,cols,diag1,diag2)

        cols.remove(col)
        diag1.remove(row-col)
        diag2.remove(row+col)
        
        
    return cnt

print(bt(0,set(),set(),set()))