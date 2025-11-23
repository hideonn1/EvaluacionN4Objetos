-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `rut` VARCHAR(12) NOT NULL,
  `nombres` VARCHAR(80) NOT NULL,
  `apellido_paterno` VARCHAR(45) NOT NULL,
  `apellido_materno` VARCHAR(45) NULL,
  `email` VARCHAR(150) NOT NULL,
  `contraseña` VARCHAR(255) NOT NULL,
  `rol` VARCHAR(20) NOT NULL,
  `telefono` VARCHAR(15) NULL,
  `fecha_nacimiento` DATE NULL,
  `fecha_registro` DATE NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`destino`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`destino` (
  `id_destino` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NULL,
  `ciudad` VARCHAR(150) NULL,
  `pais` VARCHAR(11) NULL,
  `descripcion` VARCHAR(255) NULL,
  `actividades_disponibles` VARCHAR(255) NULL,
  `costo` INT NULL,
  PRIMARY KEY (`id_destino`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`paquete_turistico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`paquete_turistico` (
  `id_paquete_turistico` INT NOT NULL AUTO_INCREMENT,
  `fecha_llegada` DATETIME NULL,
  `fecha_salida` DATETIME NULL,
  `orden_visita` INT NULL,
  `costo_destino` INT NULL,
  PRIMARY KEY (`id_paquete_turistico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reserva` (
  `id_reserva` INT NOT NULL AUTO_INCREMENT,
  `fecha_inicio` DATE NULL,
  `fecha_final` DATE NULL,
  `estado` VARCHAR(15) NULL,
  `monto_total` INT NULL,
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `fk_reserva_usuario_idx` (`id_usuario` ASC),
  CONSTRAINT `fk_reserva_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `mydb`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`reserva_has_paquete_turistico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reserva_has_paquete_turistico` (
  `reserva_id_reserva` INT NOT NULL,
  `paquete_turistico_id_paquete_turistico` INT NOT NULL,
  PRIMARY KEY (`reserva_id_reserva`, `paquete_turistico_id_paquete_turistico`),
  INDEX `fk_reserva_has_paquete_turistico_paquete_turistico1_idx` (`paquete_turistico_id_paquete_turistico` ASC),
  INDEX `fk_reserva_has_paquete_turistico_reserva1_idx` (`reserva_id_reserva` ASC),
  CONSTRAINT `fk_reserva_has_paquete_turistico_reserva1`
    FOREIGN KEY (`reserva_id_reserva`)
    REFERENCES `mydb`.`reserva` (`id_reserva`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reserva_has_paquete_turistico_paquete_turistico1`
    FOREIGN KEY (`paquete_turistico_id_paquete_turistico`)
    REFERENCES `mydb`.`paquete_turistico` (`id_paquete_turistico`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`destino_has_paquete_turistico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`destino_has_paquete_turistico` (
  `destino_id_destino` INT NOT NULL,
  `paquete_turistico_id_paquete_turistico` INT NOT NULL,
  PRIMARY KEY (`destino_id_destino`, `paquete_turistico_id_paquete_turistico`),
  INDEX `fk_destino_has_paquete_turistico_paquete_turistico1_idx` (`paquete_turistico_id_paquete_turistico` ASC),
  INDEX `fk_destino_has_paquete_turistico_destino1_idx` (`destino_id_destino` ASC),
  CONSTRAINT `fk_destino_has_paquete_turistico_destino1`
    FOREIGN KEY (`destino_id_destino`)
    REFERENCES `mydb`.`destino` (`id_destino`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_destino_has_paquete_turistico_paquete_turistico1`
    FOREIGN KEY (`paquete_turistico_id_paquete_turistico`)
    REFERENCES `mydb`.`paquete_turistico` (`id_paquete_turistico`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
