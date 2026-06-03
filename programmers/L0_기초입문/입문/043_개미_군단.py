# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 03. 13:40:00

def solution(hp):
    # 장군개미(5) 마리 수 구하기
    janggun = hp // 5
    hp = hp % 5       # 남은 체력으로 hp를 업데이트
    
    # 병정개미(3) 마리 수 구하기
    byeongjeong = hp // 3
    hp = hp % 3  
    
    # 일개미(1) 마리 수 구하기
    il = hp // 1
    
    # 모든 개미의 합을 반환
    answer = janggun + byeongjeong + il
    print(answer)
    return answer