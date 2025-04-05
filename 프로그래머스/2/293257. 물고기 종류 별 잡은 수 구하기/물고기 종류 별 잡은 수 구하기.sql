-- 코드를 작성해주세요
SELECT COUNT(*) as FISH_COUNT, n.FISH_NAME
FROM FISH_INFO as i
JOIN FISH_NAME_INFO as n
ON i.FISH_TYPE = n.FISH_TYPE
GROUP BY n.FISH_NAME
ORDER BY 1 DESC