# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 05. 14:22:04

def solution(str1, str2):
    # str2가 str1 안에 포함되어 있는지 확인 
    if str2 in str1:
        # 포함되어 있다면 1 
        return 1
    # 포함되지 않았다면 2 반환
    return 2