# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 20. 11:46:59

def solution(n):
    # 7로 나눈 몫을 미리 구한다
    quotient = n // 7
    
    # 만약 나머지가 0보다 크면 quotient + 1, 
    # 아니면 quotient를 반환
    return quotient + 1 if n%7 >0 else quotient        