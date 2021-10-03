CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `trainer`;

CREATE TABLE IF NOT EXISTS `trainer` (
  `trainer_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  `engineer_name` VARCHAR(45) INT NOT NULL,
  PRIMARY KEY (`trainer_id`),
  FOREIGN KEY (`engineer_id`, `engineer_name`) REFERENCES `engineer`(`engineer_id`, `engineer_id`)
);

INSERT INTO `trainer` (`trainer_id`, `engineer_id`, `engineer_name`) VALUES
('9999', '100006', 'Ping'),
('9992', '100007', 'Min'),
('9991', '100008', 'Noi'),
('9993', '100009', 'Nom'),
('9990', '100010', 'Igle');