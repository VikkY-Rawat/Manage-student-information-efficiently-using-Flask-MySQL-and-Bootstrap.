CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
