-- Script to create users table with constraints and ensure uniqueness
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- id is auto-incrementing and primary key
    email VARCHAR(255) NOT NULL UNIQUE,  -- email must be unique and not null
    name VARCHAR(255)  -- name is a string up to 255 characters
);