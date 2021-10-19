CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `trainer`;

CREATE TABLE IF NOT EXISTS `trainer` (
  `trainer_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  PRIMARY KEY (`trainer_id`),
  FOREIGN KEY (`engineer_id`) REFERENCES `engineer`(`engineer_id`)
);

INSERT INTO `trainer` (`trainer_id`, `engineer_id`) VALUES
(9999, 100006),
(9992, 100007),
(9991, 100008),
(9993, 100009),
(9990, 100010);