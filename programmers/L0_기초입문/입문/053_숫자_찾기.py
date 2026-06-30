# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 30. 09:37:40

def solution(num, k):
    # int형 -> str형
    # int형은 하나의 덩어리라서 내부를 하나씩 뒤질 수 없음
    # str형으로 바꾸어서 내부에서 특정 숫자를 검색하거나 위치를 찾을 수 있음
    num_str = str(num)
    k_str = str(k)
    # num 안에 k가 있는지 확인 후 있으면 인덱스 + 1 숫자 반환 
    if k_str in num_str:
        return num_str.index(k_str) +1
    return -1