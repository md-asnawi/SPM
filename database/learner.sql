CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `learner`;

CREATE TABLE IF NOT EXISTS `learner` (
  `learner_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  PRIMARY KEY (`learner_id`),
  FOREIGN KEY (`engineer_id`) REFERENCES `engineer`(`engineer_id`)
);

INSERT INTO `learner` (`learner_id`, `engineer_id`) VALUES
(456, 100001),
(808, 100002),
(999, 100003),
(888, 100004),
(909, 100005);

