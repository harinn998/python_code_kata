# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 10. 17:09:23

def solution(n):
    answer = []
    # 1부터 n까지 반복
    for i in range(1, n+1): 
        # i가 n의 약수라면 (나머지가 0이라면)
        if n % i == 0:
            answer.append(i)
    return answer