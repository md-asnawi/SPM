CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `engineer_class`;

CREATE TABLE IF NOT EXISTS `engineer_class` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  `date_assigned` DATETIME NOT NULL,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `progress` INT NOT NULL,
  `enrolment_status` VARCHAR(45) NOT NULL,
  `preassigned` BOOLEAN NOT NULL,
  `withdrawal` BOOLEAN NOT NULL,
  
  PRIMARY KEY (`course_name`, `class_id`, `engineer_id`),
  FOREIGN KEY (`course_name`, `class_id`) REFERENCES `class`(`course_name`, `class_id`),
  FOREIGN KEY (`engineer_id`) REFERENCES `engineer`(`engineer_id`)
);

INSERT INTO `engineer_class` (`course_name`, `class_id`, `engineer_id`, `date_assigned`, `start_date`, `end_date`, `progress`, `enrolment_status`, `preassigned`, `withdrawal`) VALUES
('Course 111', '1', '100001', '2021-04-01', '2021-04-05', '2021-04-30', '30', 'Enrolled', 'TRUE', 'FALSE'),
('Course 111', '2', '100005', '2021-04-01', '2021-04-05', '2021-04-30', '10', 'Enrolled', 'TRUE', 'FALSE'),
('Course 111', '1', '100003', '2021-04-01', '2021-04-05', '2021-04-30', '100', 'Enrolled', 'TRUE', 'FALSE'),
('Course 222', '1', '100003', '2021-04-01', '2021-04-05', '2021-04-30', '0', 'Pending', 'fal', 'FALSE'),
('Course 333', '1', '100003', '2021-04-01', '2021-04-05', '2021-04-30', '50', 'Enrolled', 'FALSE', 'FALSE');