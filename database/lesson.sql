CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `lesson`;

CREATE TABLE IF NOT EXISTS `lesson` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  -- `material_id` INT NOT NULL, 
  `ungraded_quiz` BOOLEAN NOT NULL, 
  `completion_status` INT NOT NULL,
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `class`(`course_name`, `class_id`)
  -- FOREIGN KEY (`material_id`) REFERENCES `course_material`(`material_id`)
);

INSERT INTO `lesson` (`course_name`, `class_id`, `lesson_id`, `ungraded_quiz`, `completion_status`) VALUES
('Course 111', '1', '1', 'TRUE', '100'),
('Course 111', '1', '2', 'TRUE', '0'),
('Course 222', '1', '3', 'TRUE', '0'),
('Course 222', '1', '4', 'TRUE', '20'),
('Course 444', '1', '5', 'TRUE', '40');