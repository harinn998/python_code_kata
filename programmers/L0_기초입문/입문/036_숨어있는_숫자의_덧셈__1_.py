# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 09. 14:47:44

def solution(my_string):
    # 숫자 누적 합 변수 초기화
    total = 0
    for char in my_string:
        # 현재 char가 숫자로 변환 가능한 형태인지 확인
        if char.isdigit():
            # str 상태인 숫자를 int로 바꾸어 합계에 더하기
            total+=int(char)
    return total