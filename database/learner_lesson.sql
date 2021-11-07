CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner_lesson`;

CREATE TABLE IF NOT EXISTS `learner_lesson` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `learner_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `is_completed` BOOLEAN NOT NULL,
  
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`, `learner_id`) REFERENCES `learner_class` (`course_name`, `class_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`) REFERENCES `lesson` (`course_name`, `class_id`, `lesson_id`)
);

INSERT INTO `learner_lesson` (`course_name`, `class_id`, `learner_id`, `lesson_id`, `is_completed`) VALUES
('Ink Course', 1, 999, 1, FALSE),
('Ink Course', 1, 999, 2, FALSE),
('Ink Course', 1, 999, 3, FALSE);
