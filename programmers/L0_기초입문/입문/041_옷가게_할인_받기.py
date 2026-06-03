# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 03. 13:17:22

def solution(price):
    # 50만 원 이상 구매했을 때 
    if price>=500000:
        answer = int(price-price*0.2)
    # 30만 원 이상 구매했을 때 
    elif price >= 300000:
        answer = int(price-price*0.1)
    # 10만 원 이상 구매했을 때 
    elif price>=100000:
        answer = int(price-price*0.05)
    # 10만 원 미만 구매했을 때 
    else:
        answer = price
    return answer