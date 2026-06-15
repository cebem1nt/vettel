SELECT
    ROW_NUMBER() OVER 
        (ORDER BY "Time" ASC) AS '',
    t.*
FROM (
    SELECT 
        race.year as "Year",
        driver.name as "Driver",
        CASE 
            WHEN q.qualifying_time THEN q.qualifying_time
            WHEN q.qualifying_q1
                and (q.qualifying_q2 is NULL or q.qualifying_q1 <= q.qualifying_q2)
                and (q.qualifying_q3 is NULL or q.qualifying_q1 <= q.qualifying_q3) THEN q.qualifying_q1
            WHEN q.qualifying_q2
                and (q.qualifying_q1 is NULL or q.qualifying_q2 <= q.qualifying_q1)
                and (q.qualifying_q3 is NULL or q.qualifying_q2 <= q.qualifying_q3) THEN q.qualifying_q2
            WHEN q.qualifying_q3
                and (q.qualifying_q1 is NULL or q.qualifying_q3 <= q.qualifying_q1)
                and (q.qualifying_q2 is NULL or q.qualifying_q3 <= q.qualifying_q2) THEN q.qualifying_q3
            ELSE NULL
        END as "Time"
    FROM     
        race_data q
    JOIN
        race on race.id = q.race_id
    JOIN
        driver on driver.id = q.driver_id
    WHERE 
        q.type = 'QUALIFYING_RESULT' and
        race.circuit_id = ?
) t
WHERE 
    t."Time" is not NULL