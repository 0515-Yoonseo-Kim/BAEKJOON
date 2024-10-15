N,K = map(int,input().split())

def josep(n,k):
    num_li = [i for i in range(1,n+1)]
    result = []

    idx = 0
    while num_li:
        idx = (idx+k-1)%len(num_li)
        result.append(num_li.pop(idx))

    return list(map(str,result))


print("<"+", ".join(josep(N,K))+">")
