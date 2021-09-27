CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `engineer`;

CREATE TABLE IF NOT EXISTS `engineer` (
  `engineer_id` INT NOT NULL,
  `engineer_name` VARCHAR(45) NULL,
  `course_completed` INT NULL,
  PRIMARY KEY (`engineer_id`),
  FOREIGN KEY (`course_completed`) REFERENCES `course`(`course_id`)
);

INSERT INTO `engineer` (`engineer_id`, `engineer_name`, `course_completed`) VALUES
('100001', 'Faith', NULL),
('100002', 'Daniel', NULL),
('100003', 'Rachel', '111'),
('100004', 'Clare', NULL),
('100005', 'Nat', NULL);