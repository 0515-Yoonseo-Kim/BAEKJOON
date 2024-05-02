string = input()
num_list = [int(s) for s in string]
zero = num_list.count(0)
one = len(num_list)-zero
tanos = "0"*(zero//2) + "1"*(one//2)
print(tanos)