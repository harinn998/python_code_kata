# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 05. 09:49:26

def solution(strlist):
    # 리스트 컴프리헨션 사용 
    # strlist에 있는 요소를 하나씩 꺼내어
    # len(items)로 길이를 잰 뒤
    # 그 값들을 모아 새로운 리스트 반환 
    return [len(items) for items in strlist]