-- 1. users의 데이터에서 이름이 '건우'이고, 지역 정보가 '경기도'인 데이터를 조회하시오
SELECT * FROM users
WHERE first_name = '건우' AND country = '경기도';

-- 2. users의 데이터에서 경기도 혹은 강원도에 살지 않는 사람들 중 나이가 20살 이상, 30살 이하인 사람들의 데이터를 나이를 기준 오름차순으로 조회하시오.
SELECT * FROM users
WHERE country NOT IN ('경기도', '강원도') AND age BETWEEN 20 AND 30
ORDER BY age;