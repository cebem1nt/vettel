SELECT
    sds.championship_won,
    sds.position_text as "",
    d.name as "Name",
    co.ioc_code as "Nationality",
    sds.points as "Points"
FROM
    season_driver_standing sds
LEFT JOIN
    driver d ON d.id = sds.driver_id
LEFT JOIN
    country co ON co.id = d.country_of_birth_country_id
WHERE
    sds.year = ?
ORDER BY
    sds.points DESC
    