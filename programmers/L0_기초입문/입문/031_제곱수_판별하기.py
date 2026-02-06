# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 06. 09:21:31

import math # 수학 계산을 위한 모듈 불러오기 

def solution(n):
    # 입력받은 숫자 n의 제곱근 구하기 
    x= math.sqrt(n) 
    # 제곱근 x를 정수로 변환했을 때 원래의 x와 같은지 비교
    if int(x) == x:
        # 제곱수일 경우 1
        return 1
    # 제곱수가 아닐 경우 2 반환
    return 2
    