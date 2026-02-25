# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 25. 09:28:16

def solution(array):
    # 리스트를 오름차순으로 정렬 (원본이 변경됨)
    array.sort()
    # 전체 길이를 2로 나눈 몫을 인덱스로 사용하여 중앙값 반환
    return array[len(array)//2]