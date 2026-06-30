# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 30. 09:28:17

def solution(array):
    # 정렬 없이 바로 가장 큰 수 찾기
    max_num = max(array)   
    # 가장 큰 수의 인덱스와 함께 결과 반환
    return max_num, array.index(max_num) 