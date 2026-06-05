SELECT 
    rd.race_fastest_lap as "Is Fastest Lap",
    rd.race_pole_position as "Is Pole",
    rd.race_reason_retired as "Reason Retired",
    rds.positions_gained as "Points Pos Gained",
    fl.fastest_lap_gap as "Gap to Fastest",
    rd.race_positions_gained as "Gained",
    rd.race_time_penalty as "Penalty",
    rd.position_text as "Finish",
    d.name as "Driver",
    c.name as "Constructor",
    rd.race_grid_position_text as "Start",
    rd.race_gap as "Gap",
    rd.race_laps as "Laps", 
    rd.race_pit_stops as "Pits",
    fl.fastest_lap_lap as "Fastest Lap",
    fl.fastest_lap_time as "Fastest Lap Time",
    rds.position_text as "Pts Pos",
    rd.race_points as "Pts"
FROM 
    race_data rd
JOIN 
    race on race.id = rd.race_id
JOIN
    driver d on d.id = rd.driver_id
JOIN
    constructor c on c.id = rd.constructor_id    
LEFT JOIN    
    race_data fl on fl.race_id = rd.race_id
    and fl.driver_id = rd.driver_id
    and fl.type = 'FASTEST_LAP'
LEFT JOIN
    race_driver_standing rds on rds.race_id = race.id
    and rds.driver_id = rd.driver_id
WHERE 
    rd.type = 'RACE_RESULT' and
    (race.grand_prix_id = :id or race.circuit_id = :id) and 
    race.year = :year