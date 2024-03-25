import sys
input = sys.stdin.readline

# N -> 포켓몬 수, Q -> 문제 수
N,M=map(int,input().split())
pokemon_dict = {}

for i in range(1,N+1):
    name = input().rstrip()
    pokemon_dict[name] = str(i)
    pokemon_dict[str(i)] = name


for _ in range(M):
    print(pokemon_dict[input().rstrip()])

    