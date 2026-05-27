SELECT
    r.qualifying_date,
    gp.name,
    d.name,
    co.ioc_code,
    COALESCE(q.time, q.q3) AS time,
    c.name,
    q.laps
FROM
    qualifying_result q
LEFT JOIN
    race r ON r.id = q.race_id
LEFT JOIN
    grand_prix gp ON r.grand_prix_id = gp.id
LEFT JOIN
    driver d ON d.id = q.driver_id
LEFT JOIN
    constructor c ON c.id = q.constructor_id
LEFT JOIN
    country co ON co.id = d.country_of_birth_country_id
WHERE
    r.year = ? AND q.position_number = 1