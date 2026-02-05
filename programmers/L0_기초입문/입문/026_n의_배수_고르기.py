# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 05. 09:34:54

def solution(n, numlist):
    answer = []
    # numlist에 있는 숫자들 하나씩 꺼내서 확인
    for items in numlist:
        # items를 n으로 나눈 나머지가 0인지 확인 
        if items % n == 0:
            answer.append(items) # 조건에 맞으면 answer 리스트에 추가 
    return answer
