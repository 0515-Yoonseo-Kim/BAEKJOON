
def solution(str1, str2):
    str1,str2=str1.upper(),str2.upper()
    str1_set=dict()
    str2_set=dict()
    str1_element=0
    str2_element=0
    for i in range(1,len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            str1_element+=1
            pair = str1[i-1]+str1[i]
            if pair in str1_set:
                str1_set[pair]+=1
            else:
                str1_set[pair]=1
    for i in range(1,len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            str2_element+=1
            pair = str2[i-1]+str2[i]
            if pair in str2_set:
                str2_set[pair]+=1
            else:
                str2_set[pair]=1
    setA= set([k for k,_ in str1_set.items()])
    setB= set([k for k,_ in str2_set.items()])
    
    denominator = 0
    numerator = 0
    
    for i in list(setA&setB):
        numerator += min(str1_set[i],str2_set[i])
    
    for i in list(setA|setB):
        if i in setA:
            denominator += str1_set[i]
        if i in setB:
            denominator += str2_set[i]
        if i in setA and i in setB:
            denominator -= min(str1_set[i],str2_set[i])
            
    
    return 65536*(numerator/denominator)//1 if denominator!= 0 else 65536
    
    
