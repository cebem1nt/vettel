SELECT 
    rd.race_fastest_lap as "Is Fastest Lap",
    rd.race_pole_position as "Is Pole",
    rd.race_reason_retired as "Reason Retired",
    rds.positions_gained as "Points Pos Gained",
    fl.fastest_lap_gap as "Gap to Fastest",
    rd.race_positions_gained as "Gained",
    rd.race_time_penalty as "Penalty", 
    gp.name as "GP",
    c.name as "Constructor",
    rd.race_grid_position_text as "Start",
    rd.position_text as "Finish",
    rd.race_gap as "Gap",
    rd.race_laps as "Laps", 
    rd.race_pit_stops as "Pits",
    fl.fastest_lap_time as "Fastest Lap Time",
    fl.fastest_lap_lap as "Fastest Lap",
    rds.position_text as "Pts Pos",
    rds.points as "Pts"
FROM 
    race_data rd
JOIN 
    race r on r.id = rd.race_id
JOIN
    constructor c on c.id = rd.constructor_id
JOIN
    grand_prix gp on gp.id = r.grand_prix_id
LEFT JOIN    
    race_data fl on fl.race_id = rd.race_id
    and fl.driver_id = :id 
    and fl.type = 'FASTEST_LAP'
LEFT JOIN
    race_driver_standing rds on rds.race_id = r.id
    and rds.driver_id = :id    
WHERE 
    rd.driver_id = :id and 
    rd.type = 'RACE_RESULT'