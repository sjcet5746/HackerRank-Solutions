--Written by Gskd
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiouAEIOU]';
