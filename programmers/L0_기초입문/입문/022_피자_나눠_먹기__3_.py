# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 22. 09:33:27

def solution(slice, n):
    # n명을 slice 조각으로 나누었을 때 나머지가 있는지 확인
    if n % slice != 0:
        # 있다면 한 판이 더 필요하므로 1
        remain = 1 
    else:
        # 없다면 한 판이 필요없으므로 0
        remain = 0
    # 전체 인원을 조각 수로 나눈 몫에 추가 판 수를 더해 반환
    return (n //slice) + remain