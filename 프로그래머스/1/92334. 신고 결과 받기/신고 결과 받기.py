def solution(id_list, report, k):
    
    complaint = {user:set() for user in id_list}
    mail = {user: 0 for user in id_list}
    
    for r in report:
        re,reported = r.split()
        complaint[reported].add(re)    
    
    
    suspension = [key for key,val in complaint.items() if len(val)>=k]
    for s in suspension:
        temp_list = list(complaint[s])
        for t in temp_list:
            mail[t]+=1
    
    
    result = list(mail.values())
    return result
    
