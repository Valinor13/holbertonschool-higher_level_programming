-- Lists all shows in database without a linked genre

SELECT title, genre_id 
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON tsg.show_id = ts.id
WHERE tsg.genre_id IS NULL
ORDER BY
ts.title, tsg.genre_id ASC;
