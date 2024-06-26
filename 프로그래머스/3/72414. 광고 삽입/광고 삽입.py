def time_to_sec(time: str) -> int:
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

def sec_to_time(seconds: int) -> str:
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    ptime = time_to_sec(play_time)
    adtime = time_to_sec(adv_time)
    timeline = [0] * (ptime + 1)
    
    for log in logs:
        start, end = log.split('-')
        start = time_to_sec(start)
        end = time_to_sec(end)
        timeline[start] += 1
        if end <= ptime:
            timeline[end] -= 1

    for i in range(1, ptime + 1):
        timeline[i] += timeline[i - 1]

    for i in range(1, ptime + 1):
        timeline[i] += timeline[i - 1]

    max_viewers = timeline[adtime - 1]
    max_start_time = 0

    for start_time in range(1, ptime - adtime + 1):
        end_time = start_time + adtime - 1
        current_viewers = timeline[end_time] - timeline[start_time - 1]
        if current_viewers > max_viewers:
            max_viewers = current_viewers
            max_start_time = start_time

    return sec_to_time(max_start_time)