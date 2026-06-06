SELECT
    pit.pit_stop_time_millis,
    grand_prix.name,
    pit.pit_stop_lap,
    pit.pit_stop_time
FROM
    race_data pit
JOIN 
    race r on r.id = pit.race_id
JOIN
    grand_prix on grand_prix.id = r.grand_prix_id
WHERE
    pit.type = 'PIT_STOP' and
    pit.driver_id = :id and r.year = :year