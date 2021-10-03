CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner`;

CREATE TABLE IF NOT EXISTS `learner` (
  `learner_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  `engineer_name` VARCHAR(45) INT NOT NULL,
  `course_completed` INT NULL,
  PRIMARY KEY (`learner_id`),
  FOREIGN KEY (`engineer_id`, `engineer_name`) REFERENCES `engineer`(`engineer_id`, `engineer_id`),
  FOREIGN KEY (`course_completed`) REFERENCES `engineer`(`course_id`)
);

INSERT INTO `learner` (`learner_id`, `engineer_id`, `engineer_name`, `course_completed`) VALUES
('456', '100001', 'Faith', NULL),
('007', '100002', 'Daniel', NULL),
('653', '100003', 'Rachel', '111'),
('888', '100004', 'Clare', NULL),
('001', '100005', 'Nat', NULL);