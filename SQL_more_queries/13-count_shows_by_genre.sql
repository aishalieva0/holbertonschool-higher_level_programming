-- ists all genres from hbtn_0d_tvshows and displays the number of shows
SELECT g.name genre, COUNT(g.id) number_of_shows FROM tv_genres g
	LEFT JOIN tv_show_genres tg ON g.id = tg.genre_id
	GROUP BY (g.id)
	ORDER BY number_of_shows DESC;
