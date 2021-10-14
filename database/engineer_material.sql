CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `engineer_material`;

CREATE TABLE IF NOT EXISTS `engineer_material` (
  `course_id` INT NOT NULL,
  `engineer_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `status` VARCHAR(45) NULL,
  
  PRIMARY KEY (`course_id`, `engineer_id`, `material_id`),
  FOREIGN KEY (`course_id`) REFERENCES `course`(`course_id`),
  FOREIGN KEY (`engineer_id`) REFERENCES `engineer`(`engineer_id`),
  FOREIGN KEY (`material_id`) REFERENCES `material`(`material_id`)
);

INSERT INTO `engineer_material` (`course_id`, `engineer_id`, `material_id`, `status`) VALUES
('111', '100001', '1', 'Incomplete'),
('111', '100005', '1', 'Incomplete'),
('333', '100003', '1', 'Incomplete'),
('555', '100003', '1', 'Incomplete'),
('555', '100002', '1', 'Completed');