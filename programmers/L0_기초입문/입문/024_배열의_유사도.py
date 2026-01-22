# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 22. 09:52:05

def solution(s1, s2):
    # 집합(set)으로 만든 뒤 교집합(&)을 구하고 그 개수를 센다
    return len(set(s1) & set(s2))