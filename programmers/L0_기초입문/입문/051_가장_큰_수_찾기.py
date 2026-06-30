# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 30. 09:26:26

def solution(array):
    # 원본 배열 오름차순 정렬한 새로운 리스트 생성 
    array2=sorted(array)
    # 정렬된 리스트의 맨 마지막 요소와 원본 배열에서 가장 큰 수의 인덱스 구함 
    answer= array2[-1],array.index(array2[-1])
    return answer