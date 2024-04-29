from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    today = list(today.split('.'))
    today_date = datetime(int(today[0]), int(today[1]), int(today[2]))
    term = dict()
    for t in terms:
        t = t.split()
        term[t[0]] = int(t[1])
    
    result = []

    # main
    for idx, p in enumerate(privacies):
        date, num = p.split()
        date = date.split('.')
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        if date+relativedelta(months=term[num]) <= today_date:
            result.append(idx+1)
 
    return result
