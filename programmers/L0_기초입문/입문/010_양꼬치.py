# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 16. 15:39:03

def solution(n, k):
    if n >= 10:
        total = 12000*n + 2000*(k-((n)//10))
    else: 
        total = 12000*n + 2000*k
    return total