# 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157339
# 작성자: 박하린
# 작성일: 2026. 01. 19. 11:25:03

-- 코드를 입력하세요
SELECT a.CAR_ID, a.CAR_TYPE, ROUND(a.DAILY_FEE * 30 * (1-c.DISCOUNT_RATE/100),0) FEE
FROM CAR_RENTAL_COMPANY_CAR a
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN c
ON a.CAR_TYPE = c.CAR_TYPE
WHERE a.CAR_TYPE IN ('세단', 'SUV')
                AND c.DURATION_TYPE like '30일 이상%'
                AND a.CAR_ID NOT IN(SELECT b.CAR_ID
                      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY b
                      WHERE DATE_FORMAT(b.START_DATE, '%Y-%m-%d')<= '2022-11-30' 
                      AND b.END_DATE >= '2022-11-01')
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE desc, a.CAR_TYPE, a.CAR_ID desc