import datetime
import heapq
def solution(m, musicinfos):
    which_music={}
    replace_dict={'C#':'X','B#':'Q','D#':'W','F#':'J','G#':'L','A#':'N','C':'Z','D':'Y','E':'H','F':'I','G':'K','A':'M','B':'O'}
    def replace(rhy):
        for k,v in replace_dict.items():
            rhy=rhy.replace(k,v)
        return rhy
    m=replace(m)

    for music in musicinfos:
        st,ed,title,rhythm = music.split(',')
        rhythm=replace(rhythm)
        st=datetime.datetime.strptime(st,'%H:%M')
        ed=datetime.datetime.strptime(ed,'%H:%M')
        diff = str(ed-st)
        h,minute,_=diff.split(':')
        total = int(h)*60+int(minute)
        new_rhythm = rhythm*(total//len(rhythm))+rhythm[:total%len(rhythm)]
        which_music[title]=new_rhythm
        
    correct=[]
    
    print(which_music)
    for title, rhythm in which_music.items():
        rhythm=replace(rhythm)
        if m in rhythm:
            
            heapq.heappush(correct,[-len(rhythm),title])
    
    return heapq.heappop(correct)[1] if correct else "(None)"
