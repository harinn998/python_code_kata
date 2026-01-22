# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 22. 09:41:39

def solution(dot):
    # 리스트의 값을 x와 y로 각각 나누기 
    x, y = dot  
    # 각 좌표 부호 확인하여 사분면 판별 
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
    