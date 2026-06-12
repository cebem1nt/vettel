SELECT 
    r.round, gp.name, c.name,
        r.date, r.time, 
        r.sprint_race_date, r.sprint_race_time, 
        r.qualifying_date, r.qualifying_time, 
        r.sprint_qualifying_date, r.sprint_qualifying_time
FROM 
    race r
LEFT JOIN
    grand_prix gp ON gp.id = r.grand_prix_id
LEFT JOIN
    circuit c on c.id = r.circuit_id
WHERE 
    r.year = ?
ORDER BY 
    r.round