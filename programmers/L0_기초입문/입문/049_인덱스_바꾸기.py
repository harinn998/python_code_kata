# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 10. 16:59:14

def solution(my_string, num1, num2):
    # 수정하기 위해 리스트로 변환 
    str_list = list(my_string)
    # num1, num2 값 서로 바꿈 
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    # 리스트를 다시 하나의 문자로 합쳐서 반환
    return "".join(str_list)