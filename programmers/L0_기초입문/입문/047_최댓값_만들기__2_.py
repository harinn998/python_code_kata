# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 10. 16:47:45

def solution(numbers):
    # 리스트를 작은 순서대로 정렬하기
    numbers.sort()
    
    # [가장 작은 음수 2개의 곱]과 [가장 큰 양수 2개의 곱] 중 큰 쪽을 반환
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])