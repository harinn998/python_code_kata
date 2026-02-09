# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 09. 09:29:35

def solution(num_list):
    # 개수를 저장할 변수 초기화
    even = 0
    odd = 0
    for item in num_list:
        # 2로 나눈 나머지가 0이면 짝수
        if item%2 == 0:
            even+=1
        # 그렇지 않으면 홀수
        else:
            odd +=1
    # 최종 결과를 [짝수 개수, 홀수 개수] 형태의 리스트로 반환
    return [even, odd]