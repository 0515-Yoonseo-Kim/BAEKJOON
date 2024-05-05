from itertools import product

def emoticon_plus(u,s):
    sub_total = 0
    for idx,e in enumerate(emoticon):
        if s[idx]>=(u[0]/100):
            sub_total += (1-s[idx])*e
    
    if sub_total<u[1]:
        return [0,int(sub_total)]
    else:
        return [1,0]
    
    
    
def solution(users, emoticons):
    global emoticon
    emoticon = emoticons
    
    plus_users=0
    total=0
    
    
    

    prod_list = list(product([0.1,0.2,0.3,0.4],repeat = len(emoticons)))

    max_users = []
    for p in prod_list:
        plus_user = 0
        sub_total = 0
        for u in users:
            check, sub = emoticon_plus(u,p)
            plus_user+=check
            sub_total+=sub

        if plus_user>plus_users:
            plus_users=plus_user
            max_users = [int(sub_total)]
            
        elif plus_user == plus_users:
            max_users.append(int(sub_total))

    total = max(max_users)
            

            
    
    
    


        
    return [plus_users,total]
