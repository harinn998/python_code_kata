# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 10. 16:52:46

def solution(cipher, code):
    # code - 1 번째 인덱스(즉, code 번째 글자)부터 시작해서, code 간격만큼 건너뛰며 가져온다
    return cipher[code - 1 :: code]