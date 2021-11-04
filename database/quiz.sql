CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `quiz`;

CREATE TABLE IF NOT EXISTS `quiz` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `quiz_id` INT NOT NULL,
  `quiz_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`, `quiz_id`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`) REFERENCES `lesson`(`course_name`, `class_id`, `lesson_id`)
);

INSERT INTO `quiz` (`course_name`, `class_id`, `lesson_id`, `quiz_id`, `quiz_type`) VALUES
('Ink Course', 1, 1, 1, 'Ungraded'),
('Ink Course', 1, 2, 2, 'Ungraded'),
('Ink Course', 1, 3, 3, 'Graded'),
('Ink Course', 2, 2, 1, 'Ungraded'),
('Ink Course', 2, 2, 2, 'Graded');

