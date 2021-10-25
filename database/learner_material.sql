CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner_material`;

CREATE TABLE IF NOT EXISTS `learner_material` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `lesson_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `learner_id` INT NOT NULL,
  `completion_status` VARCHAR(45) NULL,
  
  PRIMARY KEY (`course_name`, `class_id`, `lesson_id`, `material_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`, `lesson_id`, `material_id`) REFERENCES `material`(`course_name`, `class_id`, `lesson_id`, `material_id`),
  FOREIGN KEY (`learner_id`) REFERENCES `learner_class`(`learner_id`)
);

INSERT INTO `learner_material` (`course_name`, `class_id`, `lesson_id`, `material_id`, `learner_id`, `completion_status`) VALUES
('Course 111', 1, 1, 1, 456, 'Incomplete'),
('Course 111', 1, 1, 2, 999, 'Complete');


-- Learner class
-- course name, class id, learner id
-- 'Course 111', 1, 456 done
-- 'Course 111', 2, 909
-- 'Course 111', 1, 999 done
-- 'Course 222', 1, 999
-- 'Course 333', 1, 999
-- 'Course 111', 2, 808 done

-- Material
-- course name, class id, lesson id, material id
-- 'Course 111', 1, 1, 1
-- 'Course 111', 1, 1, 2
-- 'Course 111', 1, 2, 3
-- 'Course 111', 1, 4, 4
-- 'Course 111', 1, 4, 5
