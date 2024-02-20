CREATE DATABASE OnlineTutor;
USE OnlineTutor;
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    activation_token VARCHAR(100) UNIQUE,
    registration_completed BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    activation_token VARCHAR(100) UNIQUE,
    registration_completed BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE TABLE Accounts (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    account_type ENUM('students', 'teachers', 'tbd') NOT NULL DEFAULT 'tbd',
    activation_token VARCHAR(100) UNIQUE,
    registration_completed BOOLEAN NOT NULL DEFAULT FALSE
);
-- ALTER TABLE Students ADD COLUMN registration_complete BOOLEAN DEFAULT FALSE; 
-- ALTER TABLE Teachers ADD COLUMN registration_complete BOOLEAN DEFAULT FALSE;