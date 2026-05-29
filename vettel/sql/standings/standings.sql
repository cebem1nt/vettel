SELECT
    sds.championship_won,
    sds.position_text as "",
    d.name as "Name",
    co.ioc_code as "Nationality",
    c.name as "Constructor",
    sds.points as "Points"
FROM
    season_driver_standing sds
LEFT JOIN
    driver d ON d.id = sds.driver_id
LEFT JOIN
    country co ON co.id = d.nationality_country_id
LEFT JOIN
    season_entrant_driver sed ON sed.driver_id = d.id AND sed.year = :year
LEFT JOIN
    constructor c on c.id = sed.constructor_id
WHERE
    sds.year = :year
ORDER BY
    sds.points DESC