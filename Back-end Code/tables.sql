CREATE DATABASE OnlineTutor;
USE OnlineTutor;
CREATE TABLE Student (
    studentId INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    grade ENUM('kindergarten', 'primary', 'secondary', 'bachelor', 'graduate', 'tbd') NOT NULL DEFAULT 'tbd',
    timezone VARCHAR(50) DEFAULT 'UTC +0',
    msg VARCHAR(255) DEFAULT 'Hello, I am a student',
    activation_token VARCHAR(100) UNIQUE,
    registration_completed BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE TABLE Tutor (
    tutorId INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    eduBackground ENUM('highschool', 'bachelor', 'master', 'phd', 'tbd') NOT NULL DEFAULT 'tbd',
    timezone VARCHAR(50) DEFAULT 'UTC +0',
    availableTime VARCHAR(100) DEFAULT '',
    msg VARCHAR(255) DEFAULT 'Hello, I am a tutor',
    activation_token VARCHAR(100) UNIQUE,
    registration_completed BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE TABLE Subject (
    subjectId INT AUTO_INCREMENT PRIMARY KEY,
    subjectName VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE Student_post (
    postId INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    student_name VARCHAR(255) NOT NULL,
    subject_id INT NOT NULL,
    subject_name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    title VARCHAR(50) NOT NULL,
    msg VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2),
    available_time VARCHAR(255),
    status VARCHAR(50)
);
-- ALTER TABLE Students ADD COLUMN registration_complete BOOLEAN DEFAULT FALSE; 
-- ALTER TABLE Teachers ADD COLUMN registration_complete BOOLEAN DEFAULT FALSE;