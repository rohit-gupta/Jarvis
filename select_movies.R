movie_metadata <- read.csv("~/Downloads/movie_metadata.csv")
popular_movies <- movie_metadata[movie_metadata$num_voted_users > 100000,]
popular_movies_color <- popular_movies[popular_movies$color == "Color",]
popular_movies_color_SFW <- popular_movies_color[popular_movies_color$content_rating == "R" | popular_movies_color$content_rating == "PG-13" | popular_movies_color$content_rating == "PG" | popular_movies_color$content_rating == "G",]
popular_movies_color_SFW_English <- popular_movies_color_SFW[popular_movies_color_SFW$language == "English",]
selected_movies <- popular_movies_color_SFW_English[popular_movies_color_SFW_English$aspect_ratio == 2.35 | popular_movies_color_SFW_English$aspect_ratio == 1.85,]
selected_movies_trunc <- selected_movies[,c("movie_title","title_year","imdb_score","aspect_ratio","genres")]
write.table(selected_movies_trunc, "selected_movies.csv", sep = ",", row.names = FALSE, col.names = c("movie_title","title_year","imdb_score","aspect_ratio","genres"))