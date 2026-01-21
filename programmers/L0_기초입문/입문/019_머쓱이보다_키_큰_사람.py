# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 21. 10:49:12

def solution(array, height):
    count = 0
    # array에서 키를 하나씩 꺼내 x라고 지정
    for x in array:
        # 꺼낸 키가 height보다 큰지 확인
        if x > height:
            # 조건이 맞다면 count에 1을 더해 기록
            count+=1
    # 모든 array를 확인하고 최종적으로 합산된 count 반환 
    return count