# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 09. 12:01:03

def solution(my_string):
    result = []
    for char in my_string:
        # 현재 글자가 숫자인지 판별
        if char.isdigit():  
            # 문자 형태의 숫자를 진짜 정수(int)로 변환하여 리스트에 추가
            result.append(int(char))
    # 리스트 오름차순 정렬
    return sorted(result)