# 15. 나머지 1이 되는 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for x in range(1,n+1):
        if n%x==1:
            return x 
        else:
            continue