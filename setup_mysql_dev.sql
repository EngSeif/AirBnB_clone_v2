-- Begin by creating database and ensure it doesnt exist to not overwrite it
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Ensure all permissions on the entire database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'; FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'; FLUSH PRIVILEGES;
