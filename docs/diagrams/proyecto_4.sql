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
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `rut` VARCHAR(12) NULL,
  `nombres` VARCHAR(80) NOT NULL,
  `apellido_paterno` VARCHAR(45) NOT NULL,
  `apellido_materno` VARCHAR(45) NULL,
  `email` VARCHAR(150) NOT NULL,
  `telefono` VARCHAR(15) NULL,
  `direccion` VARCHAR(150) NULL,
  `fecha_nacimiento` DATE NULL,
  `fecha_registro` DATE NULL,
  `rol` VARCHAR(20) NOT NULL,
  `contraseña` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE INDEX `rut_UNIQUE` (`rut` ASC),
  UNIQUE INDEX `id_usuario_UNIQUE` (`id_usuario` ASC),
  UNIQUE INDEX `telefono_UNIQUE` (`telefono` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Reserva` (
  `id_reserva` INT NOT NULL AUTO_INCREMENT,
  `fecha_reserva` DATE NULL,
  `estado` VARCHAR(15) NULL,
  `monto_pagado` INT NULL,
  `Usuario_id_usuario` INT NOT NULL,
  PRIMARY KEY (`id_reserva`),
  UNIQUE INDEX `id_reserva_UNIQUE` (`id_reserva` ASC),
  INDEX `fk_Reserva_Usuario_idx` (`Usuario_id_usuario` ASC),
  CONSTRAINT `fk_Reserva_Usuario`
    FOREIGN KEY (`Usuario_id_usuario`)
    REFERENCES `mydb`.`Usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Paquete_Turistico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Paquete_Turistico` (
  `id_paquete_turistico` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NULL,
  `fecha_inicio` DATETIME NULL,
  `fecha_fin` DATETIME NULL,
  `precio_total` INT NULL,
  `cupos_disponibles` INT NULL,
  `descripcion` VARCHAR(255) NULL,
  `Reserva_id_reserva` INT NOT NULL,
  PRIMARY KEY (`id_paquete_turistico`),
  INDEX `fk_Paquete_Turistico_Reserva1_idx` (`Reserva_id_reserva` ASC),
  CONSTRAINT `fk_Paquete_Turistico_Reserva1`
    FOREIGN KEY (`Reserva_id_reserva`)
    REFERENCES `mydb`.`Reserva` (`id_reserva`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Destino`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Destino` (
  `id_destino` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NULL,
  `ciudad` VARCHAR(150) NULL,
  `pais` VARCHAR(150) NULL,
  `descripcion` VARCHAR(255) NULL,
  `actividades_disp` VARCHAR(255) NULL,
  PRIMARY KEY (`id_destino`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Destino_has_Paquete_Turistico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Destino_has_Paquete_Turistico` (
  `Destino_id_destino` INT NOT NULL,
  `Paquete_Turistico_id_paquete_turistico` INT NOT NULL,
  PRIMARY KEY (`Destino_id_destino`, `Paquete_Turistico_id_paquete_turistico`),
  INDEX `fk_Destino_has_Paquete_Turistico_Paquete_Turistico1_idx` (`Paquete_Turistico_id_paquete_turistico` ASC),
  INDEX `fk_Destino_has_Paquete_Turistico_Destino1_idx` (`Destino_id_destino` ASC),
  CONSTRAINT `fk_Destino_has_Paquete_Turistico_Destino1`
    FOREIGN KEY (`Destino_id_destino`)
    REFERENCES `mydb`.`Destino` (`id_destino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Destino_has_Paquete_Turistico_Paquete_Turistico1`
    FOREIGN KEY (`Paquete_Turistico_id_paquete_turistico`)
    REFERENCES `mydb`.`Paquete_Turistico` (`id_paquete_turistico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
