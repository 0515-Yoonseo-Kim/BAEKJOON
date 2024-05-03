string = list(input())
zero = string.count("0")//2
one = string.count("1")//2

for o in range(one):
    string.pop(string.index("1"))

string = string[::-1]
for z in range(zero):
    string.pop(string.index("0"))

string = string[::-1]
string = "".join(string)
print(string)

