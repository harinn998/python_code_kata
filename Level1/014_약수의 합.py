# 14. 약수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    total = 0
    for i in range(1,n+1):
        if n%i == 0:
            total+=i
    return total