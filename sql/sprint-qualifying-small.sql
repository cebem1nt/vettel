SELECT
    driver.name as "Driver",
    q.qualifying_q1 as "Q1",
    q.qualifying_q2 as "Q2",
    q.qualifying_q3 as "Q3",
    q.qualifying_gap as "Gap",
    r.race_grid_position_text as "Grid"
FROM
    race_data q
JOIN
    race on race.id = q.race_id
JOIN
    driver on driver.id = q.driver_id
LEFT JOIN    
    race_data r on r.race_id = q.race_id and
    r.driver_id = q.driver_id and
    r.type = 'SPRINT_RACE_RESULT'
WHERE    
    q.type = 'SPRINT_QUALIFYING_RESULT' and
    (race.grand_prix_id = :id or race.circuit_id = :id) and
    race.year = :year