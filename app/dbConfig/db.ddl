CREATE TABLE `blast_wilson_demo`.`pins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pin` VARCHAR(45) NOT NULL,
  `entity` VARCHAR(45) NULL,
  `group_id` VARCHAR(45) NULL,
  `active` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `entity_UNIQUE` (`entity` ASC) VISIBLE)
AUTO_INCREMENT = 100;

CREATE TABLE `blast_wilson_demo`.`groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(255) NULL,
  `active` TINYINT NULL,
  PRIMARY KEY (`id`));