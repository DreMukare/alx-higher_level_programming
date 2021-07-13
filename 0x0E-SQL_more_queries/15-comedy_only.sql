-- lists all comedy shows in database
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy';
