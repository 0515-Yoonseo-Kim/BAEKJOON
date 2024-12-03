SELECT 
    YEAR(e.differentiation_date) AS year,
    (m.max_size_of_colony - e.size_of_colony) AS year_dev,
    e.id
FROM 
    ecoli_data e
JOIN (
    SELECT 
        YEAR(differentiation_date) AS year,
        MAX(size_of_colony) AS max_size_of_colony
    FROM 
        ecoli_data
    GROUP BY 
        YEAR(differentiation_date)
) m
ON YEAR(e.differentiation_date) = m.year
ORDER BY 
    year ASC, year_dev ASC;
