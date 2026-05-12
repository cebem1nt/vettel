SELECT 
    gp.name,
    r.date,
    d.name,
    c.name,
    r.laps,
    rr.time
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
WHERE
    r.year = ? AND rr.position_number = 1