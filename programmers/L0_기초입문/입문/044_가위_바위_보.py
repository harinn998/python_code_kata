# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 박하린
# 작성일: 2026. 06. 09. 11:50:51

def solution(rsp):
    # 가위바위보 승리 규칙 딕셔너리
    match = {'2':'0', '0':'5', '5':'2'}
    answer = ""
    # rsp 문자열을 하나씩 승리 규칙 answer 누적 
    for char in rsp:
        answer += match[char]
    return answer