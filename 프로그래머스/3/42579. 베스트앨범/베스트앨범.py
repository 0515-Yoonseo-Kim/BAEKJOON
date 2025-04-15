from collections import defaultdict

def solution(genres, plays):
    genre_to_musics = defaultdict(list)
    
    # 1. 장르별 노래 리스트에 (재생 수, 고유 번호) 추가
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_to_musics[g].append((p, i))

    # 2. 장르별 총 재생 수 기준으로 정렬
    genre_order = sorted(genre_to_musics.keys(), key=lambda g: -sum(p for p, _ in genre_to_musics[g]))
    
    answer = []
    for g in genre_order:
        # 3. 장르 내에서 (재생 수 내림차순, index 오름차순)
        songs = sorted(genre_to_musics[g], key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in songs[:2]])
    
    return answer
