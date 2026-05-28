SELECT
    scs.championship_won,
    scs.position_text as "",
    c.name as "Name",
    scs.points as "Points"
FROM
    season_constructor_standing scs
LEFT JOIN    
    constructor c ON c.id = scs.constructor_id
WHERE
    scs.year = ?
ORDER BY
    scs.points DESC