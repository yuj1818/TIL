SELECT R.CAR_ID, R.CAR_TYPE, ROUND(R.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
FROM
    (
        SELECT C.CAR_ID, C.CAR_TYPE, C.DAILY_FEE
        FROM (
            CAR_RENTAL_COMPANY_CAR C JOIN
            CAR_RENTAL_COMPANY_RENTAL_HISTORY H
            ON C.CAR_ID = H.CAR_ID
        )
        WHERE C.CAR_ID NOT IN (
            SELECT CAR_ID 
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
        ) AND CAR_TYPE IN ('SUV','세단')
    ) R JOIN (
        SELECT CAR_TYPE, DISCOUNT_RATE
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE DURATION_TYPE LIKE '30%'
    ) P ON R.CAR_TYPE = P.CAR_TYPE
GROUP BY CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC