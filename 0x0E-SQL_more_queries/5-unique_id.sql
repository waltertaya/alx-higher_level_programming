-- script that creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT default 1 UNIQUE,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
