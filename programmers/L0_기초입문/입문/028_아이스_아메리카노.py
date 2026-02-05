# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 05. 14:17:22

def solution(money):
    # 구매 가능한 개수를 알기 위해 몫 구하기
    price = 5500
    n = money // price 
    # 나머지 구하기 
    r = money % price
    # 리스트로 반환
    return [n,r]