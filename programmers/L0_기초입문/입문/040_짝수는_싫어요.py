# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 03. 13:01:43

def solution(n):
    i=0
    answer = []
    while i <= n:
        if i%2==1:
            answer.append(i)
        i+=1 
    return answer