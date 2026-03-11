SELECT 
    r.round, gp.name, r.date, r.sprint_race_date, r.qualifying_date, r.sprint_qualifying_date
FROM 
    race r
LEFT JOIN
    grand_prix gp ON gp.id = r.grand_prix_id
WHERE 
    r.year = ?
ORDER BY 
    r.round