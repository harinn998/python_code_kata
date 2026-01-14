# 10. 배열의 평균값
# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    sum=0
    for i in numbers:
        sum += i
    return sum / len(numbers)