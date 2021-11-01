CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `lesson`;

CREATE TABLE IF NOT EXISTS `lesson` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `description`  VARCHAR(45) NOT NULL, 
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `class`(`course_name`, `class_id`)
);

INSERT INTO `lesson` (`course_name`, `class_id`, `lesson_id`, `description`) VALUES
('Course 111', 1, 1, 'This is Lesson 1'),
('Course 111', 1, 2, 'This is Lesson 2'),
('Course 111', 1, 3, 'This is Lesson 3'),
('Course 111', 2, 1, 'This is Lesson 1'),
('Course 111', 2, 2, 'This is Lesson 2'),
('Course 222', 1, 1, 'This is Lesson 1'),
('Course 222', 1, 2, 'This is Lesson 2');
