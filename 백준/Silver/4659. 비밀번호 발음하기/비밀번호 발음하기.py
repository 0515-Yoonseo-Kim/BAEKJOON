import sys
input =sys.stdin.readline
def check(string):
    vowels = ["a","e","i","o","u"]
    cnt_c = 0
    cnt_v = 0
    memo = ""
    check = False
    for s in string:
        if s!= memo or s in ["e","o"]:
            if s in vowels:
                cnt_v+=1
                cnt_c=0
                check=True
            else:
                cnt_c+=1
                cnt_v=0
            memo = s
        else:
          return False
        if cnt_c>=3 or cnt_v>=3:
            return False


    if check:
        return True
    else:
        return False

def print_check(s):
    if s == "end":
        return

    if check(s):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")


while True:
    s = input().rstrip()
    if s == "end":
        break
    else:
        print_check(s)

