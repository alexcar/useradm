DROP TABLE IF EXISTS tbl_user;

CREATE TABLE tbl_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_name VARCHAR(45) NOT NULL,
    user_username VARCHAR(45) NOT NULL,
    user_password VARCHAR(45) NOT NULL
);
