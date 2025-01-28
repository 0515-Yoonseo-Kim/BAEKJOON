T = int(input())

def find_ancestor(num):
    ancs = set()
    while num >= 1:
        ancs.add(num)
        num//=2
    return ancs


for _ in range(T):
    n1, n2 = map(int,input().split())
    print(10 * max(find_ancestor(n1)&find_ancestor(n2)))