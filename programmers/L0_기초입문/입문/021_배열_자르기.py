# 배열 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120833
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 21. 11:01:50

def solution(numbers, num1, num2):
    # 슬라이싱 문법 [start : end]에서 end 인덱스는 결과에 포함되지 않으므로, 
    # num2 인덱스까지 포함하기 위해 num2 + 1을 끝점으로 지정
    return numbers[num1:num2+1] 
