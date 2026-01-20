# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 20. 11:54:55

def solution(numbers):
    # 리스트를 오름차순으로 정렬
    numbers.sort()
    # 정렬된 리스트에서 가장 큰 값(마지막 원소)과 
    # 두 번째로 큰 값(뒤에서 두 번째 원소)을 곱하여 반환
    return numbers[-1] * numbers[-2]