SELECT 
    r.date as "Date",
    gp.name as "GP",
    d.name as "Winner",
    co.ioc_code "Nationality",
    c.name "Constructor",
    r.laps "Laps",
    rr.time "Time",
    rr.grid_position_text "Grid"
FROM
    race_result rr
LEFT JOIN
    race r ON r.id = rr.race_id
LEFT JOIN
    grand_prix gp ON r.grand_prix_id = gp.id
LEFT JOIN
    driver d ON d.id = rr.driver_id
LEFT JOIN
    constructor c ON c.id = rr.constructor_id
LEFT JOIN
    country co ON co.id = d.country_of_birth_country_id
WHERE
    r.year = ? AND rr.position_number = 1