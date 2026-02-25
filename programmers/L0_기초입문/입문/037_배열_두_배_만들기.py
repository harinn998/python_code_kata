# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 25. 09:12:30

def solution(numbers):
    # 리스트 컴프리헨션을 사용하여
    # 각 요소를 2배로 만든 리스트 반환 
    return [n*2 for n in numbers]
        