-- Lists all shows with all genres linked to it

SELECT title, name
FROM tv_genres tg
RIGHT JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
RIGHT JOIN tv_shows ts
ON tsg.show_id = ts.id
ORDER BY title, name;
