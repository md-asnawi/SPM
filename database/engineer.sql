CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `engineer`;

CREATE TABLE IF NOT EXISTS `engineer` (
  `engineer_id` INT NOT NULL,
  `engineer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`engineer_id`)
);

INSERT INTO `engineer` (`engineer_id`, `engineer_name`) VALUES
(100001, 'Faith'),
(100002, 'Daniel'),
(100003, 'Rachel'),
(100004, 'Clare'),
(100005, 'Nat'),
(100006, 'Ping'),
(100007, 'Min'),
(100008, 'Noi'),
(100009, 'Nom'),
(100010, 'Igle');