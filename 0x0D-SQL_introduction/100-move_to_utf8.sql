-- converts a database to UTF8 encoding.
USE `hbtn_0c_0`;
ALTER TABLE `first_table`
CONVET TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
