-- lists all shows without the genre Comedy
SELECT s.title FROM tv_shows s
WHERE s.id NOT IN
(SELECT s.id FROM  tv_show_genres tg
	JOIN tv_genres g ON tg.genre_id=g.id
	JOIN tv_shows s ON tg.show_id= s.id WHERE g.name='Comedy')
ORDER BY s.title
