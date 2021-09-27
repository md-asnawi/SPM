CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `engineer_class`;

CREATE TABLE IF NOT EXISTS `engineer_class` (
  `course_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  `date_assigned` DATETIME NOT NULL,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `status` VARCHAR(45) NULL,
  
  PRIMARY KEY (`course_id`, `class_id`, `engineer_id`),
  FOREIGN KEY (`course_id`) REFERENCES `course`(`course_id`),
  FOREIGN KEY (`class_id`) REFERENCES `class`(`class_id`),
  FOREIGN KEY (`engineer_id`) REFERENCES `engineer`(`engineer_id`)
);

INSERT INTO `engineer_class` (`course_id`, `class_id`, `engineer_id`, `date_assigned`, `start_date`, `end_date`, `status`) VALUES
('111', '1', '100001', '2021-04-01', '2021-04-05', '2021-04-30', 'Incomplete'),
('111', '2', '100005', '2021-04-01', '2021-04-05', '2021-04-30', 'Incomplete'),
('333', '1', '100003', '2021-04-01', '2021-04-05', '2021-04-30', 'Incomplete'),
('555', '1', '100003', '2021-04-01', '2021-04-05', '2021-04-30', 'Incomplete'),
('555', '2', '100002', '2021-04-01', '2021-04-05', '2021-04-30', 'Completed')