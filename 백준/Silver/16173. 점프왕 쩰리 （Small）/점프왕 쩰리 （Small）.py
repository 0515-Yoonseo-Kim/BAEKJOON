N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


def dfs(x,y):
    num = arr[x][y]
    if num == -1:
        return "HaruHaru"
    if num == 0:
        return "Hing"
    if x+num<N:
        result = dfs(x+num,y)
        if result == "HaruHaru":
            return "HaruHaru"
    if y+num<N:
        result = dfs(x,y+num)
        if result == "HaruHaru":
            return "HaruHaru"

    return "Hing"

print(dfs(0,0))
