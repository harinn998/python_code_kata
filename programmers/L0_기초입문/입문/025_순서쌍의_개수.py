# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 22. 11:05:58

def solution(n):
    count = 0
    # 1부터 n까지 모든 숫자를 하나씩 꺼내어 i로 반복 
    for i in range(1,n+1):
        # n을 i로 나누었을 때 나머지가 0인지 확인
        # 0 이면 약수라는 뜻 
        if n % i == 0:
            # 약수가 확인될 때마다 순서쌍이 하나 존재하므로 count를 1
            count +=1
    return count