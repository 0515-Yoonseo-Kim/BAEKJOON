def convert_to_int(str_time:str) -> int:
    m,s = map(int,str_time.split(":"))
    return 60*m+s

def convert_to_time(int_time:int) -> str:
    m,s = str(int_time//60).zfill(2),str(int_time%60).zfill(2)
    return ":".join([m,s])

def solution(video_len, pos, op_start, op_end, commands):
    total_time,current_time,op_start,op_end = map(convert_to_int,[video_len,pos,op_start,op_end])
    for command in commands:
        if op_start<=current_time<op_end:
            current_time = op_end
        if command == "next":
            current_time = min(current_time+10,total_time)
        else:
            current_time = max(current_time-10,0)
        if op_start<=current_time<op_end:
            current_time = op_end
    return convert_to_time(current_time)