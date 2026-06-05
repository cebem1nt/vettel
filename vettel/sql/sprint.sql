SELECT
    r.race_positions_gained as "Gained",
    r.race_reason_retired as "Reason Retired",
    r.race_time_penalty as "Penalty",
    r.position_text as "Finish",
    driver.name as "Driver",
    constructor.name as "Contructor",
    r.race_grid_position_text as "Start",
    r.race_gap as "Gap",
    r.race_laps as "Laps",
    r.race_points as "Pts"
FROM
    race_data r
JOIN
    race on race.id = r.race_id
JOIN
    driver on driver.id = r.driver_id
JOIN    
    constructor on constructor.id = r.constructor_id
WHERE    
    r.type = 'SPRINT_RACE_RESULT' and
    (race.grand_prix_id = :id or race.circuit_id = :id) and
    race.year = :year