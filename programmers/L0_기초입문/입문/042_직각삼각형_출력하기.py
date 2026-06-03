# 직각삼각형 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120823
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 03. 13:23:43

n = int(input())
for i in range(n):
    # i는 0부터 시작, 별의 개수 맞추기 위해 i+1로 설정
    # 문자열에 '*'에 곱하여 숫자만큼 문자 반복
    print((i+1)*'*')