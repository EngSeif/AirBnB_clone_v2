-- The same code on the setup_mysql_dev.sql but the difference is this only for tests
-- Hbnb test instead of hbnb dev
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Ensure previlage
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Push previlage
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
