SELECT 
    r.date,
    gp.name,
    d.name,
    co.ioc_code,
    c.name,
    r.laps,
    rr.time,
    rr.grid_position_text
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