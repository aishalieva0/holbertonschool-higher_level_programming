-- lists all genres by their rating
SELECT g.name, SUM(r.rate) rating FROM tv_show_genres tg
JOIN tv_genres g ON tg.genre_id=g.id
JOIN tv_show_ratings r ON tg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
