# 문자열 정렬하기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 30. 09:31:14

def solution(my_string):
    # 소문자로 변환 (리스트 형식으로 저장됨)
    sort_string = sorted(my_string.lower())
    # 리스트를 다시 빈틈없는 문자열로 합치기 
    return "".join(sort_string)