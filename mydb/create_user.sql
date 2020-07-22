CREATE USER 'usera'@'%' IDENTIFIED WITH mysql_native_password BY '123';

GRANT ALL PRIVILEGES ON bot .* TO 'usera'@'%';