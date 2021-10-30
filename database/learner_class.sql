CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner_class`;

CREATE TABLE IF NOT EXISTS `learner_class` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `learner_id` INT NOT NULL,
  `date_assigned` DATETIME NOT NULL,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `progress` INT NOT NULL,
  `enrolment_status` VARCHAR(45) NOT NULL,
  `preassigned` BOOLEAN NOT NULL,
  `withdrawal` BOOLEAN NOT NULL,
  `withdrawal_message` VARCHAR(255) NULL,
  
  PRIMARY KEY (`course_name`, `class_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `class`(`course_name`, `class_id`),
  FOREIGN KEY (`learner_id`) REFERENCES `learner`(`learner_id`)
);

INSERT INTO `learner_class` (`course_name`, `class_id`, `learner_id`, `date_assigned`, `start_date`, `end_date`, `progress`, `enrolment_status`, `preassigned`, `withdrawal`, `withdrawal_message`) VALUES
('Course 111', 1, 456, '2021-04-01', '2021-04-05', '2021-04-30', 30, 'Enrolled', 'TRUE', 'FALSE', NULL),
('Course 111', 2, 909, '2021-04-01', '2021-04-05', '2021-04-30', 10, 'Enrolled', 'TRUE', 'FALSE', NULL),
('Course 111', 1, 999, '2021-04-01', '2021-04-05', '2021-04-30', 100, 'Enrolled', 'TRUE', 'FALSE', NULL),
('Course 222', 1, 999, '2021-04-01', '2021-04-05', '2021-04-30', 0, 'Pending', 'FALSE', 'FALSE', NULL),
('Course 333', 1, 999, '2021-04-01', '2021-04-05', '2021-04-30', 50, 'Enrolled', 'FALSE', 'FALSE', NULL),
('Course 111', 2, 808, '2021-04-01', '2021-04-05', '2021-04-30', 50, 'Pending', 'FALSE', 'FALSE', NULL);