CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `lesson`;

CREATE TABLE IF NOT EXISTS `lesson` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `description`  VARCHAR(45) NOT NULL, 
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `Class`(`course_name`, `class_id`)
);

INSERT INTO `lesson` (`course_name`, `class_id`, `lesson_id`, `description`) VALUES
('Ink Course', 1, 1, 'This is Lesson 1'),
('Ink Course', 1, 2, 'This is Lesson 2'),
('Ink Course', 1, 3, 'This is Lesson 3'),
('Ink Course', 2, 1, 'This is Lesson 1'),
('Ink Course', 2, 2, 'This is Lesson 2'),
('Ink Course', 2, 3, 'This is Lesson 3'),
('Ink Course', 2, 4, 'This is Lesson 4'),
('Ink Course', 2, 5, 'This is Lesson 5'),
('Data Course', 1, 1, 'This is Lesson 1'),
('Data Course', 1, 2, 'This is Lesson 2'),
('Data Course', 1, 3, 'This is Lesson 3'),
('Data Course', 1, 4, 'This is Lesson 4'),
('Data Course', 1, 5, 'This is Lesson 5'),
('Printer Course', 1, 1, 'This is Lesson 1'),
('Design Course', 1, 1, 'This is Lesson 1'),
('Drawing Course', 1, 1, 'This is Lesson 1');
