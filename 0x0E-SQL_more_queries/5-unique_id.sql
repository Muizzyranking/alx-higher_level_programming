-- creates a table with defaults to 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
