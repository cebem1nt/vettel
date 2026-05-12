SELECT
    sds.championship_won,
    sds.position_text,
    d.name,
    sds.points
FROM
    season_driver_standing sds
LEFT JOIN    
    driver d ON d.id = sds.driver_id
WHERE
    sds.year = ?
ORDER BY
    sds.points DESC