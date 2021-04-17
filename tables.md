CREATE DATABSE weather;

CREATE TABLE IF NOT EXISTS weather (
	id serial NOT NULL,
	coord_lon float8 NULL,
	coord_lat float8 NULL,
	temp numeric(10, 2) NULL,
	feels_like numeric(10, 2) NULL,
	temp_min numeric(10, 2) NOT NULL,
	temp_max numeric(10, 2) NOT NULL,
	pressure numeric(10, 2) NULL,
	humidity numeric(10, 2) NULL,
	sea_level numeric(10, 2) NULL,
	grnd_level integer NULL,
	visibility numeric(10, 2) NULL,
	wind_speed numeric(10, 2) NULL,
	wind_deg numeric(10, 2) NULL,
	wind_gust numeric(10, 2) NULL,
	clouds_all numeric(10, 2) NULL,
	country varchar(2) NULL,
	sunrise timestamp NULL,
	sunset timestamp NULL,
	city varchar(50) NULL,
	primary key(id)
);