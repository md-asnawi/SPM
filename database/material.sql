CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `material`;

CREATE TABLE IF NOT EXISTS `material` (
  `material_id` INT NOT NULL,
  `material_name` VARCHAR(45) NULL,
  `format` VARCHAR(45) NULL,
  `material_type` VARCHAR(45) NULL,
  `uploader` INT NOT NULL,
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  PRIMARY KEY (`material_id`),
  FOREIGN KEY (`uploader`) REFERENCES `engineer`(`engineer_id`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`) REFERENCES `lesson`(`course_name`, `class_id`, `lesson_id`)
);

INSERT INTO `material` (`material_id`, `material_name`, `format`, `material_type`, `uploader`, `course_name`, `class_id`, `lesson_id`) VALUES
('1', 'Material 1', NULL, 'Quiz', '100001', 'Course 111', 1, 1),
('2', 'Material 2', NULL, 'Learning Package', '100002', 'Course 111', 1, 1), 
('3', 'Material 3', NULL, 'Quiz', '100002', 'Course 111', 1, 2),
('4', 'Material 4', NULL, 'Quiz', '100001', 'Course 222', 1, 4),
('5', 'Material 5', NULL, 'Learning Package', '100002', 'Course 222', 1, 4);