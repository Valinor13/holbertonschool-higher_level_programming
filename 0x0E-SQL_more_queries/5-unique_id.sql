-- Creates a table with 2 keys
-- unique_id(id default 1, name)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	UNIQUE (ID),
	name VARCHAR(256) NOT NULL
);
