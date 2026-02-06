# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 06. 09:37:34

def solution(my_string):
    # 제거해야 할 모음 리스트
    vowels = ['a','e','i','o','u']
    
    # 각 모음을 하나씩 꺼내어 반복 
    for items in vowels:
        # my_string에서 해당 모음 제거한 뒤
        # 다시 my_string에 업데이트 
        my_string = my_string.replace(items, "")
    return my_string