# 문자 반복 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 05. 14:29:12

def solution(my_string, n):
    # 결과 담을 빈 문자열
    a = ''
    # 문자열의 글자 하나씩 꺼내기
    for items in my_string:
        # 각 글자 n번 반복하여 a에 추가 
        a+=(items*n)
    return a