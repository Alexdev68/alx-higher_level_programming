-- This script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name FROM tv_genres, tv_show_genres Where tv_show_genres.show_id = 8 and tv_show_genres.genre_id = tv_genres.id ORDER BY tv_genres.name ASC
