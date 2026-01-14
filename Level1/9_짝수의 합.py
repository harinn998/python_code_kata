# 9. 짝수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    sum = 0 
    for i in range(0, n+1,2):
        sum+=i
    return sum