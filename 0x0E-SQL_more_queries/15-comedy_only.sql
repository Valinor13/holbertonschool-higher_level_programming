-- Lists all Comedy shows in the database.

SELECT title
FROM tv_genres tg
INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON tsg.show_id = ts.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title;
