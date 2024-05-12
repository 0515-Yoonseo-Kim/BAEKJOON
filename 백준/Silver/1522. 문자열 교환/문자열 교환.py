string = input()

num_a = string.count("a")
new_str = string+string[:-1]
min_change = string.count("b")

iter = len(new_str)-num_a

for i in range(iter):
    min_change = min(min_change,num_a-new_str[i:i+num_a].count("a"))

print(min_change)