# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 20. 11:50:18

def solution(n, t):
    result = n
    for i in range(1,t+1):
        result = (result * 2)
    return result 