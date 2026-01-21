# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 01. 21. 10:56:22

def solution(sides):
    # 가장 긴 변을 마지막으로 보내기 위해 sort(오름차순)로 정리 
    sides.sort()
    # 삼각형 성립 조건: 가장 긴 변 < 나머지 두 변의 합
    if sides[-1] < sides[0]+sides[1]:
        # 조건에 부합하면 1 반환
        return 1
    # 조건에 부합하지 않으면 2 반환
    return 2