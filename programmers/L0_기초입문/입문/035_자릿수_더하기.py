# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 09. 09:42:47

def solution(n):
    # n을 문자열로 변환
    # map을 통해 문자열의 각 글자를 하나씩 꺼내 int로 변환
    # sum으로 모두 합산하여 결과 반환
    return sum(map(int, str(n)))