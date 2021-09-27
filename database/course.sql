CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `course`;

CREATE TABLE IF NOT EXISTS `course` (
  `course_id` INT NOT NULL,
  `course_name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `prereq` INT NULL,
  PRIMARY KEY (`course_id`),
  FOREIGN KEY (`prereq`) REFERENCES `course`(`course_id`)
);

INSERT INTO `course` (`course_id`, `course_name`, `description`, `prereq`) VALUES
('111', 'Course 111', 'This is Course 111', NULL),
('222', 'Course 222', 'This is Course 222', NULL),
('333', 'Course 333', 'This is Course 333', '111'),
('444', 'Course 444', 'This is Course 444', '333'),
('555', 'Course 555', 'This is Course 555', NULL);