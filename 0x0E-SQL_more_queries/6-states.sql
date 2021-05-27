-- Creates a database and table.
-- hbtn_0d_usa, states(id, name)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT, 
	UNIQUE (ID),
	PRIMARY KEY (ID),
	name VARCHAR(256) NOT NULL
);
