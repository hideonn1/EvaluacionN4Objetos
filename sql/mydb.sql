-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2025 at 11:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `mydb`;

-- --------------------------------------------------------

--
-- Table structure for table `destino`
--

CREATE TABLE `destino` (
  `id_destino` int(11) NOT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `ciudad` varchar(150) DEFAULT NULL,
  `pais` varchar(40) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `actividades_disponibles` varchar(255) DEFAULT NULL,
  `costo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `destino`
--

INSERT INTO `destino` (`id_destino`, `nombre`, `ciudad`, `pais`, `descripcion`, `actividades_disponibles`, `costo`) VALUES
(1, 'mi_casa', 'valdivia', '11', 'valdivia es lo mas grande', 'costanera', 35000),
(3, 'Inacap', 'Valdivia', '0', 'Inacap es una universidad', 'Estudiar', 2000000),
(4, 'Casino de Inacap', 'Valdivia', '0', 'Este es el casino que esta dentro de Inacap', 'Comprar comida', 3900),
(5, 'Plaza de Armas', 'Santiago', 'Chile', 'Aqui vive Boric', 'Tirar piedras', 7000000),
(6, 'Supermercado El Trebol', 'Valdivia', 'Chile', 'Este es un supermercado', 'Venden cosas como pan', 990);

-- --------------------------------------------------------

--
-- Table structure for table `destino_has_paquete_turistico`
--

CREATE TABLE `destino_has_paquete_turistico` (
  `destino_id_destino` int(11) NOT NULL,
  `paquete_turistico_id_paquete_turistico` int(11) NOT NULL,
  `fecha_salida` datetime DEFAULT NULL,
  `fecha_llegada` datetime DEFAULT NULL,
  `orden_visita` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `destino_has_paquete_turistico`
--

INSERT INTO `destino_has_paquete_turistico` (`destino_id_destino`, `paquete_turistico_id_paquete_turistico`, `fecha_salida`, `fecha_llegada`, `orden_visita`) VALUES
(1, 1, NULL, NULL, NULL),
(5, 8, NULL, NULL, 1),
(5, 9, NULL, NULL, 1),
(5, 12, NULL, NULL, 1),
(5, 14, NULL, NULL, 1),
(5, 15, NULL, NULL, 1),
(5, 16, NULL, NULL, 1),
(5, 17, NULL, NULL, 1),
(5, 18, NULL, NULL, 1),
(6, 6, NULL, NULL, 1),
(6, 7, NULL, NULL, 1),
(6, 10, NULL, NULL, 1),
(6, 11, NULL, NULL, 1),
(6, 13, NULL, NULL, 1),
(6, 18, NULL, '2025-12-14 00:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `paquete_turistico`
--

CREATE TABLE `paquete_turistico` (
  `id_paquete_turistico` int(11) NOT NULL,
  `costo_destino` int(11) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `paquete_turistico`
--

INSERT INTO `paquete_turistico` (`id_paquete_turistico`, `costo_destino`, `fecha_inicio`, `fecha_final`) VALUES
(1, 35000, NULL, NULL),
(2, 7000000, NULL, NULL),
(3, 990, NULL, NULL),
(4, 990, NULL, NULL),
(5, 990, NULL, NULL),
(6, 990, NULL, NULL),
(7, 990, NULL, NULL),
(8, 7000000, NULL, NULL),
(9, 7000000, NULL, NULL),
(10, 990, NULL, NULL),
(11, 990, NULL, NULL),
(12, 7000000, NULL, NULL),
(13, 990, NULL, NULL),
(14, 7000000, NULL, NULL),
(15, 7000000, NULL, NULL),
(16, 7000000, NULL, NULL),
(17, 7000000, NULL, NULL),
(18, 7000000, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reserva`
--

CREATE TABLE `reserva` (
  `id_reserva` int(11) NOT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `estado` varchar(15) DEFAULT NULL,
  `monto_total` int(11) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reserva_has_paquete_turistico`
--

CREATE TABLE `reserva_has_paquete_turistico` (
  `reserva_id_reserva` int(11) NOT NULL,
  `paquete_turistico_id_paquete_turistico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `nombres` varchar(80) NOT NULL,
  `apellido_paterno` varchar(45) NOT NULL,
  `apellido_materno` varchar(45) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `destino`
--
ALTER TABLE `destino`
  ADD PRIMARY KEY (`id_destino`);

--
-- Indexes for table `destino_has_paquete_turistico`
--
ALTER TABLE `destino_has_paquete_turistico`
  ADD PRIMARY KEY (`destino_id_destino`,`paquete_turistico_id_paquete_turistico`),
  ADD KEY `fk_destino_has_paquete_turistico_paquete_turistico1_idx` (`paquete_turistico_id_paquete_turistico`),
  ADD KEY `fk_destino_has_paquete_turistico_destino1_idx` (`destino_id_destino`);

--
-- Indexes for table `paquete_turistico`
--
ALTER TABLE `paquete_turistico`
  ADD PRIMARY KEY (`id_paquete_turistico`);

--
-- Indexes for table `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `fk_reserva_usuario_idx` (`id_usuario`);

--
-- Indexes for table `reserva_has_paquete_turistico`
--
ALTER TABLE `reserva_has_paquete_turistico`
  ADD PRIMARY KEY (`reserva_id_reserva`,`paquete_turistico_id_paquete_turistico`),
  ADD KEY `fk_reserva_has_paquete_turistico_paquete_turistico1_idx` (`paquete_turistico_id_paquete_turistico`),
  ADD KEY `fk_reserva_has_paquete_turistico_reserva1_idx` (`reserva_id_reserva`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `destino`
--
ALTER TABLE `destino`
  MODIFY `id_destino` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `paquete_turistico`
--
ALTER TABLE `paquete_turistico`
  MODIFY `id_paquete_turistico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `destino_has_paquete_turistico`
--
ALTER TABLE `destino_has_paquete_turistico`
  ADD CONSTRAINT `fk_destino_has_paquete_turistico_destino1` FOREIGN KEY (`destino_id_destino`) REFERENCES `destino` (`id_destino`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_destino_has_paquete_turistico_paquete_turistico1` FOREIGN KEY (`paquete_turistico_id_paquete_turistico`) REFERENCES `paquete_turistico` (`id_paquete_turistico`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `fk_reserva_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `reserva_has_paquete_turistico`
--
ALTER TABLE `reserva_has_paquete_turistico`
  ADD CONSTRAINT `fk_reserva_has_paquete_turistico_paquete_turistico1` FOREIGN KEY (`paquete_turistico_id_paquete_turistico`) REFERENCES `paquete_turistico` (`id_paquete_turistico`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_reserva_has_paquete_turistico_reserva1` FOREIGN KEY (`reserva_id_reserva`) REFERENCES `reserva` (`id_reserva`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
