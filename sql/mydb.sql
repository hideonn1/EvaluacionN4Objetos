-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2025 at 10:13 PM
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
(1, 'Torres del Paine', 'Puerto Natales', 'Chile', 'Parque con picos de granito y glaciares. Ideal para el trekking patagónico.', 'Trekking, Observación de fauna, Kayak', 55000),
(2, 'Valle de la Luna', 'San Pedro de Atacama', 'Chile', 'Paisaje desértico que simula la superficie lunar, famoso por sus atardeceres.', 'Senderismo, Observación de estrellas, Tour en bicicleta', 30000),
(3, 'Valparaíso', 'Valparaíso', 'Chile', 'Ciudad puerto, Patrimonio de la Humanidad, conocida por sus cerros y ascensores.', 'Recorrido por cerros, Visita a museos, Ascensores históricos', 25000),
(4, 'Pucón', 'Pucón', 'Chile', 'Capital de la aventura en el sur, a orillas del Lago Villarrica y cerca del volcán.', 'Ascenso al Volcán, Rafting, Termas, Deportes náuticos', 38000),
(5, 'Isla de Pascua (Rapa Nui)', 'Hanga Roa', 'Chile', 'Isla polinésica famosa por los Moais. Centro de historia y cultura ancestral.', 'Visita a Moais, Buceo, Playa Anakena', 120000),
(6, 'Carretera Austral', 'Coyhaique', 'Chile', 'Ruta escénica que atraviesa la Patagonia, con fiordos y bosques.', 'Ruta en auto, Camping, Pesca con mosca', 70000),
(7, 'Santiago - Centro', 'Santiago', 'Chile', 'Capital de Chile, mezcla de edificios históricos, modernos y áreas verdes.', 'Museos, Palacio de La Moneda, Barrio Lastarria', 15000),
(8, 'Laguna San Rafael', 'Puerto Río Tranquilo', 'Chile', 'Famoso por el ventisquero San Rafael y su laguna azul con témpanos de hielo.', 'Navegación, Avistamiento de fauna marina', 90000),
(9, 'Viña del Mar', 'Viña del Mar', 'Chile', 'Ciudad jardín costera con amplias playas, parques y el famoso Reloj de Flores.', 'Playa, Muelle Vergara, Casino', 22000),
(10, 'Parque Nacional Lauca', 'Putre', 'Chile', 'Famoso por el Lago Chungará, uno de los más altos del mundo, y su fauna andina.', 'Observación de aves, Senderismo de altura, Vistas al Volcán Parinacota', 45000),
(11, 'Copacabana', 'Río de Janeiro', 'Brasil', 'Famosa playa en forma de media luna. Hogar del Cristo Redentor y el Pan de Azúcar.', 'Vóley playa, Natación, Teleférico, Visita al Corcovado', 50000),
(12, 'Cataratas del Iguazú', 'Foz do Iguaçu', 'Brasil', 'Impresionante conjunto de cascadas compartidas con Argentina, rodeadas de selva.', 'Recorridos en bote, Senderismo en el parque, Vistas panorámicas', 65000),
(13, 'Praia do Forte', 'Mata de São João', 'Brasil', 'Pueblo costero conocido por sus playas y la reserva de tortugas marinas (Proyecto Tamar).', 'Buceo, Proyecto Tamar, Relax en la playa', 40000),
(14, 'Salvador de Bahía', 'Salvador', 'Brasil', 'Capital cultural afrobrasileña, famosa por el Pelourinho y su vibrante música.', 'Explorar Pelourinho, Clases de Capoeira, Gastronomía local', 35000),
(15, 'Amazonas', 'Manaus', 'Brasil', 'Corazón de la selva amazónica, con biodiversidad única y el encuentro de los ríos.', 'Paseos en canoa, Avistamiento de fauna, Visita a tribus', 85000),
(16, 'Florianópolis', 'Florianópolis', 'Brasil', 'Isla con más de 40 playas, conocida por su surf, dunas y lagunas.', 'Surf, Sandboard en dunas, Senderismo costero', 30000),
(17, 'Búzios', 'Búzios', 'Brasil', 'Antiguo pueblo de pescadores popularizado por Brigitte Bardot, con hermosas calas.', 'Buceo, Paseos en barco, Vida nocturna en la Rua das Pedras', 42000),
(18, 'Ouro Preto', 'Ouro Preto', 'Brasil', 'Ciudad colonial Patrimonio de la Humanidad, rica en arquitectura barroca y minas de oro.', 'Visita a iglesias barrocas, Museos, Minas históricas', 28000),
(19, 'Recife y Olinda', 'Recife', 'Brasil', 'Recife (Venecia brasileña) y Olinda (centro histórico colonial y carnavalesco).', 'Visita a Olinda, Playas urbanas, Frevo y carnaval', 33000),
(20, 'Chapada Diamantina', 'Lençóis', 'Brasil', 'Parque Nacional de mesetas y cañones. Ideal para el ecoturismo.', 'Cascadas, Grutas, Trekking a mesetas', 48000),
(21, 'Glaciar Perito Moreno', 'El Calafate', 'Argentina', 'Masa de hielo espectacular conocida por sus rupturas y pasarelas de observación.', 'Excursión sobre el glaciar (Minitrekking), Navegación', 75000),
(22, 'Buenos Aires - Centro', 'Buenos Aires', 'Argentina', 'Capital cosmopolita. Famosa por el tango, teatros y su arquitectura europea.', 'Visita al Obelisco, Teatro Colón, San Telmo y Caminito', 20000),
(23, 'Ushuaia', 'Ushuaia', 'Argentina', 'La \"Ciudad del Fin del Mundo\". Punto de partida hacia la Antártida.', 'Tren del Fin del Mundo, Navegación por el Canal Beagle, Trekking en el Parque Nacional', 60000),
(24, 'Mendoza', 'Mendoza', 'Argentina', 'Región vitivinícola líder mundial, al pie de la Cordillera de los Andes.', 'Degustación de vinos, Tour por bodegas, Aventura en montaña', 35000),
(25, 'Puerto Madryn', 'Puerto Madryn', 'Argentina', 'Capital de las actividades subacuáticas y avistamiento de fauna marina (ballenas).', 'Avistamiento de Ballenas (en temporada), Buceo con lobos marinos', 52000),
(26, 'Bariloche', 'San Carlos de Bariloche', 'Argentina', 'Centro de esquí y turismo de aventura en la Patagonia andina. Famoso por sus chocolates.', 'Esquí, Senderismo, Circuito Chico, Chocolaterías', 40000),
(27, 'Salta y Jujuy', 'Salta', 'Argentina', 'Región del Norte con cultura andina, cerros de colores y tradiciones coloniales.', 'Quebrada de Humahuaca, Tren a las Nubes, Vinos de altura', 32000),
(28, 'Peninsula Valdés', 'Puerto Pirámides', 'Argentina', 'Reserva natural con colonias de elefantes marinos, pingüinos y aves.', 'Observación de fauna marina, Safaris terrestres', 58000),
(29, 'Córdoba', 'Córdoba', 'Argentina', 'Famosa por sus universidades, arquitectura jesuítica y su vida cultural.', 'Manzana Jesuítica, Visita a las Sierras, Museos', 27000),
(30, 'Rosario', 'Rosario', 'Argentina', 'Cuna de la bandera argentina, importante puerto y centro cultural.', 'Monumento a la Bandera, Paseo por la Costanera, Museos', 24000);

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
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `rut`, `nombres`, `apellido_paterno`, `apellido_materno`, `email`, `contraseña`, `rol`, `telefono`, `fecha_nacimiento`, `fecha_registro`) VALUES
(1, '12345678-9', 'Admin', 'Sistema', 'Principal', 'admin@admin.cl', '$2b$12$BpM6YxY9Mh6BaBllbSKO4OvH362uguAwyNqKrW3lvp9aeOHToPL4S', 'Administrador', '+56 9 1234 5678', '1990-01-01', '2025-11-29'),
(2, '98765432-1', 'Cliente', 'Prueba', 'Test', 'cliente@cliente.cl', '$2b$12$cbxQoXJlzE9aFW9NRVHeMuljXIHv85rVxmSkc2afQEAgAyJloLyrC', 'Cliente', '+56 9 8765 4321', '1995-06-15', '2025-11-29');

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
  MODIFY `id_destino` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `paquete_turistico`
--
ALTER TABLE `paquete_turistico`
  MODIFY `id_paquete_turistico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
