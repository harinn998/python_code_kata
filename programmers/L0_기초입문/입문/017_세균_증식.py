# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 20. 11:51:15

def solution(n, t):
    # 초기 세균의 수(n)를 결과 변수에 저장
    result = n
    # 1부터 t시간까지 반복
    for i in range(1,t+1):
        # 매 시간마다 현재 세균의 수에 2를 곱해 업데이트
        result = (result * 2)
    return result 