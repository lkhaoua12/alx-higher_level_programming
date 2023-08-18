-- 1-create_user.sql
-- creat new user with password
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL PRIVILIGES ON *.* TO 'user_0d_1'@'localhost';
