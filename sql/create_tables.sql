CREATE TABLE IF NOT EXISTS movies (
	id varchar NOT NULL,
	"name" varchar NOT NULL,
	rating int8 NULL,
	CONSTRAINT movies_pk PRIMARY KEY (id)
);