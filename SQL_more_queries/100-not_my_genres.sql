-- to list all genres not linked to the show Dexter
SELECT g.name FROM tv_genres g
	WHERE g.id NOT IN
		(SELECT g.id FROM  tv_show_genres tg
		JOIN tv_genres g ON tg.genre_id=g.id
		JOIN tv_shows s ON tg.show_id= s.id
		WHERE s.title='Dexter')
		ORDER BY g.name
