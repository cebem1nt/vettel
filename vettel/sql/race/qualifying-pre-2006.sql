SELECT
    driver.name as "Driver",
    constructor.name as "Constructor",
    q.qualifying_time as "Time",
    q.qualifying_gap as "Gap",
    q.qualifying_laps as "Laps",
    r.race_grid_position_text as "Grid"
FROM
    race_data q
JOIN
    race on race.id = q.race_id
JOIN
    driver on driver.id = q.driver_id
JOIN    
    constructor on constructor.id = q.constructor_id
LEFT JOIN    
    race_data r on r.race_id = q.race_id and
    r.driver_id = q.driver_id and
    r.type = 'RACE_RESULT'
WHERE    
    q.type = 'QUALIFYING_RESULT' and
    (race.grand_prix_id = :id or race.circuit_id = :id) and
    race.year = :year