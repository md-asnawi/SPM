CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `quiz_question`;

CREATE TABLE IF NOT EXISTS `quiz_question` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `quiz_id` INT NOT NULL,
  `question_number` INT NOT NULL, 
  `question` VARCHAR(255) NOT NULL, 
  `question_type` VARCHAR(45) NOT NULL,
  `option_1` VARCHAR(45) NOT NULL,
  `option_2` VARCHAR(45) NOT NULL,
  `option_3` VARCHAR(45) NULL,
  `option_4` VARCHAR(45) NULL,
  `answer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`, `quiz_id`, `question_number`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`, `quiz_id`) REFERENCES `quiz`(`course_name`, `class_id`, `lesson_id`, `quiz_id`)
);

INSERT INTO `quiz_question` (`course_name`, `class_id`, `lesson_id`, `quiz_id`, `question_number`, `question`, `question_type`, `option_1`, `option_2`, `option_3`, `option_4`, `answer`) VALUES
('Ink Course', 1, 1, 1, 1, 'The ink is black', 'TF', 'True', 'False', NULL, NULL, 'True'),
('Ink Course', 1, 1, 1, 2, 'The ink is purple', 'TF', 'True', 'False', NULL, NULL, 'False'),
('Ink Course', 1, 1, 1, 3, 'Black, Pink or Purple Ink', 'MCQ', 'Black', 'Pink', 'Purple', NULL, 'Black'),
('Ink Course', 1, 2, 2, 1, 'The ink is Orange', 'TF', 'True', 'False', NULL, NULL, 'False'),
('Ink Course', 1, 2, 2, 2, 'Red or Blue', 'MCQ', 'Red', 'Blue', NULL, NULL, 'Blue'),
('Ink Course', 1, 3, 3, 1, 'The ink is Pink', 'TF', 'True', 'False', NULL, NULL, 'False'),
('Ink Course', 1, 3, 3, 2, 'The ink is Red', 'TF', 'True', 'False', NULL, NULL, 'True'),
('Ink Course', 1, 3, 3, 3, 'Red, Blue, Green or Yellow', 'MCQ', 'Red', 'Blue', 'Green', 'Yellow', 'Blue');