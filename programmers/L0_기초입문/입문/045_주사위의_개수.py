# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 09. 11:56:45

def solution(box, n):
    # 각 방향(가로, 세로, 높이)의 주사위 개수를 먼저 구한 뒤, 모두 곱해 총 개수를 계산
    return (box[0] // n) * (box[1] // n) * (box[2] // n)