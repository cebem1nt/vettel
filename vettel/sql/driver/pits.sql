SELECT
    pit.pit_stop_time_millis as "Time MS",
    grand_prix.name as "GP",
    pit.pit_stop_lap as "Lap",
    pit.pit_stop_time as "Time"
FROM
    race_data pit
JOIN 
    race r on r.id = pit.race_id
JOIN
    grand_prix on grand_prix.id = r.grand_prix_id
WHERE
    pit.type = 'PIT_STOP' and
    pit.driver_id = :id and r.year = :year