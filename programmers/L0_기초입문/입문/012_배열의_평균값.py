# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 16. 15:42:56

def solution(numbers):
    sum=0
    for i in numbers:
        sum += i
    return sum / len(numbers)