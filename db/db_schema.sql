-- -----------------------------------------------------
-- Schema farm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `farm` ;
USE `farm` ;

-- -----------------------------------------------------
-- Table `farm`.`familles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`familles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`animaux`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`animaux` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `famille_id` INT NOT NULL,
  `sexe` VARCHAR(1) NULL,
  `presence` TINYINT NULL,
  `apprivoise` TINYINT NULL,
  `mort_ne` TINYINT NULL,
  `decede` TINYINT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_animaux_familles_idx` (`famille_id` ASC) VISIBLE,
  CONSTRAINT `fk_animaux_familles`
    FOREIGN KEY (`famille_id`)
    REFERENCES `farm`.`familles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`types` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`animaux_types`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`animaux_types` (
  `animal_id` INT NOT NULL,
  `type_id` INT NOT NULL,
  `pourcentage` INT NULL,
  INDEX `fk_animaux_types_animaux1_idx` (`animal_id` ASC) VISIBLE,
  INDEX `fk_animaux_types_types1_idx` (`type_id` ASC) VISIBLE,
  CONSTRAINT `fk_animaux_types_animaux1`
    FOREIGN KEY (`animal_id`)
    REFERENCES `farm`.`animaux` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_animaux_types_types1`
    FOREIGN KEY (`type_id`)
    REFERENCES `farm`.`types` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`velages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`velages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `mere_id` INT NOT NULL,
  `pere_id` INT NOT NULL,
  `date_naissance` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_velages_animaux1_idx` (`mere_id` ASC) VISIBLE,
  INDEX `fk_velages_animaux2_idx` (`pere_id` ASC) VISIBLE,
  CONSTRAINT `fk_velages_animaux1`
    FOREIGN KEY (`mere_id`)
    REFERENCES `farm`.`animaux` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_velages_animaux2`
    FOREIGN KEY (`pere_id`)
    REFERENCES `farm`.`animaux` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`animaux_velages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`animaux_velages` (
  `annimal_id` INT NOT NULL,
  `velage_id` INT NOT NULL,
  INDEX `fk_animaux_velages_animaux1_idx` (`annimal_id` ASC) VISIBLE,
  INDEX `fk_animaux_velages_velages1_idx` (`velage_id` ASC) VISIBLE,
  CONSTRAINT `fk_animaux_velages_animaux1`
    FOREIGN KEY (`annimal_id`)
    REFERENCES `farm`.`animaux` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_animaux_velages_velages1`
    FOREIGN KEY (`velage_id`)
    REFERENCES `farm`.`velages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`complications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`complications` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `complication` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farm`.`velages_complications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `farm`.`velages_complications` (
  `velage_id` INT NOT NULL,
  `complication_id` INT NOT NULL,
  INDEX `fk_velages_complications_velages1_idx` (`velage_id` ASC) VISIBLE,
  INDEX `fk_velages_complications_complications1_idx` (`complication_id` ASC) VISIBLE,
  CONSTRAINT `fk_velages_complications_velages1`
    FOREIGN KEY (`velage_id`)
    REFERENCES `farm`.`velages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_velages_complications_complications1`
    FOREIGN KEY (`complication_id`)
    REFERENCES `farm`.`complications` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
