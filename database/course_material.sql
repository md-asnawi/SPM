CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `course_material`;

CREATE TABLE IF NOT EXISTS `course_material` (
  `material_id` INT NOT NULL,
  `material_name` VARCHAR(45) NULL,
  `material_type` VARCHAR(45) NULL,
  `course_name` VARCHAR(45) NULL,
  PRIMARY KEY (`material_id`),
  FOREIGN KEY (`course_name`) REFERENCES `course`(`course_name`)
);

INSERT INTO `course_material` (`material_id`, `material_name`, `material_type`, `course_name`) VALUES
(898456, 'Material 111', 'docx', 'Course 111'),
(564866, 'Material 222', 'pptx', 'Course 111'),
(364252, 'Material 333', 'pdf', 'Course 222'),
(364253, 'Material 444', 'mp4', 'Course 222'),
(135495, 'Material 555', 'hyperlinks', 'Course 444');