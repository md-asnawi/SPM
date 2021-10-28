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
('Course 111', 1, 1, 1, 1, 'Is this True?', 'TF', 'True', 'False', NULL, NULL, 'True'),
('Course 111', 1, 1, 1, 2, 'Is this Really True?', 'TF', 'True', 'False', NULL, NULL, 'False'),
('Course 111', 1, 1, 1, 3, 'A or B or C?', 'MCQ', 'A', 'B', 'C', NULL, 'A'),
('Course 111', 1, 1, 2, 1, 'Is this True?', 'TF', 'True', 'False', NULL, NULL, 'False'),
('Course 111', 1, 1, 2, 2, 'Is this Really Really True?', 'TF', 'True', 'False', NULL, NULL, 'True'),
('Course 111', 1, 1, 2, 3, 'A or B or C or D?', 'MCQ', 'A', 'B', 'C', NULL, 'B');