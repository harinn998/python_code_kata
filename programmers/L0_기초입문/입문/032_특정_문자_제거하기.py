# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 02. 06. 09:31:54

def solution(my_string, letter):
    # replace(찾을 문자, 바꿀 문자) 함수를 호출
    # 'letter'에 해당하는 모든 문자를 찾아 빈 문자열로 치환하여 제거
    # 3. 만약 my_string 안에 letter가 없더라도 replace는 에러 없이 원본을 그대로 반환
    return my_string.replace(letter, "")

        