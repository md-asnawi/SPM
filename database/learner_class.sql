CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner_class`;

CREATE TABLE IF NOT EXISTS `learner_class` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `learner_id` INT NOT NULL,
  `date_assigned` DATETIME NOT NULL,
  `progress` INT NOT NULL,
  `enrolment_status` VARCHAR(45) NOT NULL,
  `preassigned` BOOLEAN NOT NULL,
  `withdrawal` BOOLEAN NOT NULL,
  `withdrawal_message` VARCHAR(255) NULL,
  
  PRIMARY KEY (`course_name`, `class_id`, `learner_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `class`(`course_name`, `class_id`),
  FOREIGN KEY (`learner_id`) REFERENCES `learner`(`learner_id`)
);

INSERT INTO `learner_class` (`course_name`, `class_id`, `learner_id`, `date_assigned`, `progress`, `enrolment_status`, `preassigned`, `withdrawal`, `withdrawal_message`) VALUES
('Ink Course', 1, 456, '2021-04-01', 30, 'Enrolled', TRUE, FALSE, NULL),
('Ink Course', 2, 909, '2021-04-01', 10, 'Enrolled', TRUE, FALSE, NULL),
('Ink Course', 1, 999, '2021-04-01', 30, 'Enrolled', TRUE, FALSE, NULL),
('Ink Course', 1, 808, '2021-04-01', 0, 'Enrolled', FALSE, FALSE, NULL),
('Data Course', 1, 999, '2021-04-01', 0, 'Pending', FALSE, FALSE, NULL),
('Design Course', 1, 999, '2021-04-01', 100, 'Enrolled', FALSE, FALSE, NULL),
('Drawing Course', 1, 999, '2021-04-01', 80, 'Enrolled', FALSE, FALSE, NULL),
('Drawing Course', 2, 909, '2021-04-01', 30, 'Enrolled', FALSE, FALSE, NULL),
('Drawing Course', 2, 456, '2021-04-01', 30, 'Enrolled', TRUE, FALSE, NULL),
('Ink Course', 2, 808, '2021-04-01', 50, 'Pending', FALSE, FALSE, NULL);
