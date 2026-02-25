# 중복된 숫자 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 25. 09:16:58

def solution(array, n):
    # 리스트의 내장 메서드 count()를 사용하여 n의 개수를 직접 반환
    return array.count(n)


# 리스트 컴프리헨션 활용
'''
def solution(array, n):
    # array에서 n과 같은 요소들만 골라 새로운 리스트를 만들고
    # 그 리스트의 길이를 반환
    return len([i for i in array if i ==n])
'''

