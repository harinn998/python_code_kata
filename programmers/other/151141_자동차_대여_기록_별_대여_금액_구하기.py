# 자동차 대여 기록 별 대여 금액 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151141
# 작성자: 박하린
# 작성일: 2026. 01. 20. 10:38:08

WITH CTE AS (SELECT b.HISTORY_ID, 
             b.CAR_ID,
             DATEDIFF(b.END_DATE,b.START_DATE)+1 DIFF_DATE,
        case 
        when DATEDIFF(b.END_DATE,b.START_DATE)+1 < 7
        then 0
        when DATEDIFF(b.END_DATE,b.START_DATE)+1 < 30
        then '7일 이상'
        when DATEDIFF(b.END_DATE,b.START_DATE)+1 <90
        then '30일 이상'
        else '90일 이상'
        end as DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY b
         ) 
         
SELECT B.HISTORY_ID, 
    round(a.daily_fee * B.DIFF_DATE * ((100-IFNULL(c.discount_rate,0))/100),0) FEE
FROM CTE B
JOIN CAR_RENTAL_COMPANY_CAR a
ON B.CAR_ID = a.CAR_ID
LEFT JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN c
ON a.CAR_TYPE = c.CAR_TYPE      
AND B.DURATION_TYPE = c.DURATION_TYPE
WHERE a.CAR_TYPE = '트럭'
ORDER BY FEE desc, HISTORY_ID desc;
