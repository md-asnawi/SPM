CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner_quiz`;

CREATE TABLE IF NOT EXISTS `learner_quiz` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `quiz_id` INT NOT NULL,
  `learner_id` INT NOT NULL, 
  `score` INT NOT NULL, 
  `passboolean` BOOLEAN NOT NULL,

  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`, `quiz_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`, `quiz_id`) REFERENCES `quiz`(`course_name`, `class_id`, `lesson_id`, `quiz_id`),
  FOREIGN KEY (`learner_id`) REFERENCES `learner`(`learner_id`)
);

INSERT INTO `learner_quiz` (`course_name`, `class_id`, `lesson_id`, `quiz_id`, `learner_id`, `score`, `passboolean`) VALUES
('Course 111', 1, 1, 1, 456, 50, FALSE),
('Course 111', 1, 1, 2, 456, 100, TRUE);
