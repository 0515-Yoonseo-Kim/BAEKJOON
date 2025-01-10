def solution(bandage, health, attacks):
    cool_time,heal_per_sec,bonus_heal = bandage
    prev_time = 0
    max_health = health
    for attack in attacks:
        attack_time, damage = attack
        is_bonus = ((attack_time - prev_time - 1) >= cool_time)*((attack_time-prev_time-1)//cool_time)
        
        health = min(heal_per_sec*(attack_time-prev_time-1)+is_bonus*bonus_heal+health,max_health)
        health -= damage

        if health<=0:
            return -1
        prev_time = attack_time

    return health