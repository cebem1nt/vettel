SELECT
    ROW_NUMBER() OVER 
        (ORDER BY fastest_lap.fastest_lap_time ASC) as '',
    race.year as "Year",
    driver.name as "Driver",
    fastest_lap.fastest_lap_time as "Time",
    fastest_lap.fastest_lap_lap as "Lap"
FROM 
    race_data fastest_lap
JOIN
    race ON fastest_lap.race_id = race.id
JOIN
    driver on driver.id = fastest_lap.driver_id
WHERE 
    fastest_lap.type = 'FASTEST_LAP' 
    AND race.circuit_id = ?