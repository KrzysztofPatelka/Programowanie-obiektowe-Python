USE test;

CREATE TABLE unique_tracks(
	id_utworu VARCHAR(18) NOT NULL,
	id_wykonania VARCHAR(18) NOT NULL,
	artysta VARCHAR(373) NOT NULL,
	tytul VARCHAR(255) NOT NULL,
);

CREATE TABLE triplets_sample_20p(
	id_uzytkownika VARCHAR(40) NOT NULL,
	id_utworu VARCHAR(18) NOT NULL,
	data_odsluchania DATETIME NOT NULL
)