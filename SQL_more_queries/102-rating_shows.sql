-- lists all shows by their rating
SELECT s.title, SUM(r.rate) rating FROM tv_shows s 
	JOIN tv_show_ratings r ON s.id=r.show_id
	GROUP BY s.title
	ORDER BY rating DESC;
