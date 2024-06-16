from collections import defaultdict
userdb = dict()
message = []

def operator(command: str):
    command = command.split()
    if command[0] == "Enter":
        userdb[command[1]]=command[-1]
        message.append([1,command[1]])
    elif command[0] == "Leave":
        message.append([0,command[-1]])
        
    elif command[0]  == "Change":
        userdb[command[1]]=command[-1]
    return 

def str_mapping(li):
    c,i = li
    if c==1:
        return f"{userdb[i]}님이 들어왔습니다."
    else:
        return f"{userdb[i]}님이 나갔습니다."

def solution(record):
    for rec in record:
        operator(rec)
    return list(map(str_mapping, message))