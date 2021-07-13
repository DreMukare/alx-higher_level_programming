-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name, COUNT(*) AS number_of_shows
FROM tv_genres
GROUP BY tv_shows.name
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id;
