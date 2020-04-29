-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-12-2019 a las 04:17:11
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo21`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia`
--

CREATE TABLE `asistencia` (
  `id` int(11) NOT NULL,
  `presente` tinyint(1) NOT NULL,
  `fecha` date NOT NULL,
  `estudiante_id` int(11) NOT NULL,
  `clase_id` int(11) NOT NULL,
  `estudiante_nombre` varchar(500) NOT NULL,
  `estudiante_apellido` varchar(500) NOT NULL,
  `estudiante_documento` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `asistencia`
--

INSERT INTO `asistencia` (`id`, `presente`, `fecha`, `estudiante_id`, `clase_id`, `estudiante_nombre`, `estudiante_apellido`, `estudiante_documento`) VALUES
(44, 1, '2019-12-11', 39, 47, 'Andrés', 'Chaves', '2468'),
(45, 1, '2019-12-11', 44, 47, 'Cristian', 'Delgadillo', '5556423'),
(46, 0, '2019-12-11', 41, 47, 'Ignacio', 'Fernández', '323232'),
(47, 1, '2019-12-11', 42, 47, 'Verónica', 'Zarza', '2345'),
(48, 1, '2019-12-04', 39, 47, 'Andrés', 'Chaves', '2468'),
(49, 1, '2019-12-04', 44, 47, 'Cristian', 'Delgadillo', '5556423'),
(50, 1, '2019-12-04', 41, 47, 'Ignacio', 'Fernández', '323232'),
(51, 1, '2019-12-04', 40, 47, 'Victor', 'Stanizani', '343434'),
(52, 0, '2019-12-04', 42, 47, 'Verónica', 'Zarza', '2345');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `barrio`
--

CREATE TABLE `barrio` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `barrio`
--

INSERT INTO `barrio` (`id`, `nombre`) VALUES
(1, 'Barrio Náutico'),
(2, 'Barrio Obrero'),
(3, 'Berisso'),
(4, 'Barrio Solidaridad'),
(5, 'Barrio Obrero'),
(6, 'Barrio Bco. Pcia.'),
(7, 'Barrio J.B. Justo'),
(8, 'Barrio Obrero'),
(9, 'El Carmen'),
(10, 'El Labrador'),
(11, 'Ensenada'),
(12, 'La Hermosura'),
(13, 'La PLata'),
(14, 'Los Talas'),
(15, 'Ringuelet'),
(16, 'Tolosa'),
(17, 'Villa Alba'),
(18, 'Villa Arguello'),
(19, 'Villa B. C'),
(20, 'Villa Elvira'),
(21, 'Villa Nueva'),
(22, 'Villa Paula'),
(23, 'Villa Progreso'),
(24, 'Villa San Carlos'),
(25, 'Villa Zula');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciclo_lectivo`
--

CREATE TABLE `ciclo_lectivo` (
  `id` int(11) NOT NULL,
  `fecha_ini` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `semestre` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `ciclo_lectivo`
--

INSERT INTO `ciclo_lectivo` (`id`, `fecha_ini`, `fecha_fin`, `semestre`) VALUES
(6, '2019-07-04 00:00:00', '2019-12-14 00:00:00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciclo_lectivo_taller`
--

CREATE TABLE `ciclo_lectivo_taller` (
  `taller_id` int(11) NOT NULL,
  `ciclo_lectivo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `ciclo_lectivo_taller`
--

INSERT INTO `ciclo_lectivo_taller` (`taller_id`, `ciclo_lectivo_id`) VALUES
(13, 6),
(14, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clase`
--

CREATE TABLE `clase` (
  `id` int(11) NOT NULL,
  `dia` varchar(50) NOT NULL,
  `hora_inicio` varchar(50) NOT NULL,
  `hora_fin` varchar(50) NOT NULL,
  `taller_id` int(11) DEFAULT NULL,
  `docente_id` int(11) NOT NULL,
  `activo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clase`
--

INSERT INTO `clase` (`id`, `dia`, `hora_inicio`, `hora_fin`, `taller_id`, `docente_id`, `activo`) VALUES
(39, 'L', '10:00', '12:00', NULL, 5, 0),
(40, 'M', '10:00', '14:00', NULL, 4, 0),
(41, 'L', '11:00', '15:00', NULL, 5, 0),
(42, 'L', '00:00', '23:59', NULL, 5, 0),
(43, 'MARTES', '00:00', '23:59', NULL, 5, 0),
(44, 'LUNES', '00:00', '23:59', NULL, 6, 0),
(45, 'LUNES', '10:00', '14:00', NULL, 5, 0),
(46, 'JUEVES', '11:00', '15:00', NULL, 5, 0),
(47, 'LUNES', '15:00', '18:00', 13, 5, 1),
(48, 'MARTES', '11:00', '15:00', 13, 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configuracion`
--

CREATE TABLE `configuracion` (
  `id` int(11) NOT NULL,
  `variable` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `valor` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configuracion_sistema`
--

CREATE TABLE `configuracion_sistema` (
  `id` int(11) NOT NULL,
  `vista` varchar(255) CHARACTER SET utf16 COLLATE utf16_unicode_ci NOT NULL,
  `titulo` varchar(255) CHARACTER SET utf16 COLLATE utf16_unicode_ci NOT NULL,
  `cuerpo` varchar(5000) CHARACTER SET utf16 COLLATE utf16_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `configuracion_sistema`
--

INSERT INTO `configuracion_sistema` (`id`, `vista`, `titulo`, `cuerpo`) VALUES
(1, 'sistema', 'Paginado', '35'),
(2, 'sistema', 'Estado', '1'),
(3, 'index', 'Origen', 'LALALALALa Orquesta Escuela de Berisso comenzó a funcionar en septiembre del 2005 en el barrio de El Carmen de la localidad de Berisso bajo la dirección del Mtro. Juan Carlos Herrero, orientada especialmente a la atención de chicos en situación de vulnerabilidad socio-cultural.\r\n              Desde sus 20 alumnos iniciales fue creciendo hasta atender actualmente una matrícula de aproximadamente 530 chicos, distribuidos en los 15 núcleos que la conforman y dirigida a una franja etaria de 5 a 23 años, cubriendo en su accionar a la casi totalidad de los barrios de Berisso más los espacios cedidos por el Club Español y el Teatro Argentino.'),
(4, 'index', 'Biografia', 'La Orquesta Escuela de Berisso comenzó a funcionar en septiembre del 2005 en el barrio de El Carmen de la localidad de Berisso bajo la dirección del Mtro. Juan Carlos Herrero, orientada especialmente a la atención de chicos en situación de vulnerabilidad socio-cultural.\n              Desde sus 20 alumnos iniciales fue creciendo hasta atender actualmente una matrícula de aproximadamente 530 chicos, distribuidos en los 15 núcleos que la conforman y dirigida a una franja etaria de 5 a 23 años, cubriendo en su accionar a la casi totalidad de los barrios de Berisso más los espacios cedidos por el Club Español y el Teatro Argentino\n              En 2012 marcó la apertura de sesión en la Honorable Cámara de Diputados de la Nación durante el tratamiento de la Ley para la recuperación de YPF, realizando la grabación del Himno Nacional Argentino en el mismo lugar. Sus alumnos se han presentado en escenarios de la categoría del Salón Dorado de la Municipalidad de La Plata, las Catedrales de La Plata y Buenos Aires , Senado de la Provincia, el Coliseo Podestá, el Teatro Argentino, Centro Cultural Néstor Kirchner y el Luna Park en nuestro país; en el exterior han participado en forma grupal e individual en experiencias musicales realizadas en Venezuela, Francia, EEUU y Brasil. A partir de su formación, alumnos de la Orquesta Escuela pudieron acceder a estudios universitarios en la Facultad de Bellas Artes de La Plata y la Universidad de Lanús.'),
(5, 'index', 'Contacto', 'Tel: 0303 - 456\nDir: Bulnes 5000'),
(6, 'home', 'What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry.', 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas \"Letraset\", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente`
--

CREATE TABLE `docente` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `localidad_id` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genero_id` int(11) NOT NULL,
  `tipo_doc_id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `docente`
--

INSERT INTO `docente` (`id`, `apellido`, `nombre`, `fecha_nac`, `localidad_id`, `domicilio`, `genero_id`, `tipo_doc_id`, `numero`, `tel`) VALUES
(5, 'Fava', 'Laura', '1970-12-18', 1, 'asds 123', 2, 1, 111222333, '444555334'),
(6, 'Sánchez', 'Carlos', '1960-10-10', 9, '234 asd', 1, 1, 2332323, '333444'),
(7, 'Runco', 'Jorge', '1950-04-10', 10, 'gggd 23', 1, 1, 1555532, '1144556554');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente_clase`
--

CREATE TABLE `docente_clase` (
  `docente_id` int(11) NOT NULL,
  `clase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente_taller`
--

CREATE TABLE `docente_taller` (
  `docente_id` int(11) NOT NULL,
  `taller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `docente_taller`
--

INSERT INTO `docente_taller` (`docente_id`, `taller_id`) VALUES
(5, 13),
(6, 13),
(6, 14);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela`
--

CREATE TABLE `escuela` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefono` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `escuela`
--

INSERT INTO `escuela` (`id`, `nombre`, `direccion`, `telefono`) VALUES
(1, '502', NULL, NULL),
(2, 'Albert Thomas', NULL, NULL),
(3, 'Anexa', NULL, NULL),
(4, 'Anexo T. Speroni', NULL, NULL),
(5, 'Basiliana', NULL, NULL),
(6, 'Basiliano', NULL, NULL),
(7, 'Bellas Artes', NULL, NULL),
(8, 'Canossiano', NULL, NULL),
(9, 'Castañeda', NULL, NULL),
(10, 'Col. Nacional', NULL, NULL),
(11, 'Conquista Cristiana', NULL, NULL),
(12, 'Dardo Rocha N° 24', NULL, NULL),
(13, 'E.E.M.N° 2', NULL, NULL),
(14, 'E.M. N°26', NULL, NULL),
(15, 'E.P. Municipal N° 2', NULL, NULL),
(16, 'EE N° 2', NULL, NULL),
(17, 'EEE N° 501', NULL, NULL),
(18, 'EEE N°501', NULL, NULL),
(19, 'EEM N° 1', NULL, NULL),
(20, 'EEM N° 26 L.P', NULL, NULL),
(21, 'EEM N°128', NULL, NULL),
(22, 'EEM N°2', NULL, NULL),
(23, 'EES N° 10', NULL, NULL),
(24, 'EES N° 14', NULL, NULL),
(25, 'EES N° 4', NULL, NULL),
(26, 'EES N° 4 Berisso', NULL, NULL),
(27, 'EES N° 4 El Pino', NULL, NULL),
(28, 'EEST N° 1 bsso', NULL, NULL),
(29, 'EET Nº 1', NULL, NULL),
(30, 'EET Nº1', NULL, NULL),
(31, 'EGB N°25', NULL, NULL),
(32, 'EM N° 2', NULL, NULL),
(33, 'EMM N° 3', NULL, NULL),
(34, 'EP N° 1 L.P-', NULL, NULL),
(35, 'EP N° 11', NULL, NULL),
(36, 'EP N° 129', NULL, NULL),
(37, 'EP N° 14', NULL, NULL),
(38, 'EP N° 15', NULL, NULL),
(39, 'EP N° 17', NULL, NULL),
(40, 'EP N° 18', NULL, NULL),
(41, 'EP N° 19', NULL, NULL),
(42, 'EP N° 2', NULL, NULL),
(43, 'EP N° 20', NULL, NULL),
(44, 'EP N° 22', NULL, NULL),
(45, 'EP N° 25', NULL, NULL),
(46, 'EP N° 27', NULL, NULL),
(47, 'EP N° 3', NULL, NULL),
(48, 'EP N° 37 LP', NULL, NULL),
(49, 'EP N° 43', NULL, NULL),
(50, 'EP N° 45', NULL, NULL),
(51, 'EP N° 5', NULL, NULL),
(52, 'EP N° 6', NULL, NULL),
(53, 'EP N° 65 La Plata', NULL, NULL),
(54, 'EP N° 7', NULL, NULL),
(55, 'EPB N° 10', NULL, NULL),
(56, 'EPB N° 14', NULL, NULL),
(57, 'EPB N° 15', NULL, NULL),
(58, 'EPB N° 19', NULL, NULL),
(59, 'EPB N° 2', NULL, NULL),
(60, 'EPB N° 20', NULL, NULL),
(61, 'EPB N° 24', NULL, NULL),
(62, 'EPB N° 25', NULL, NULL),
(63, 'EPB N° 45', NULL, NULL),
(64, 'EPB N° 5', NULL, NULL),
(65, 'EPB N° 55', NULL, NULL),
(66, 'EPB N° 6', NULL, NULL),
(67, 'EPB N° 65', NULL, NULL),
(68, 'EPB N° 8', NULL, NULL),
(69, 'ESB N° 10', NULL, NULL),
(70, 'ESB N° 11', NULL, NULL),
(71, 'ESB N° 14', NULL, NULL),
(72, 'ESB N° 3', NULL, NULL),
(73, 'ESB N° 61', NULL, NULL),
(74, 'ESB N° 66', NULL, NULL),
(75, 'ESB N° 8', NULL, NULL),
(76, 'ESB N° 9', NULL, NULL),
(77, 'ESC N° 10', NULL, NULL),
(78, 'ESC N° 13', NULL, NULL),
(79, 'ESC N° 19', NULL, NULL),
(80, 'ESC N° 2', NULL, NULL),
(81, 'ESC N° 20', NULL, NULL),
(82, 'ESC N° 22', NULL, NULL),
(83, 'ESC N° 23', NULL, NULL),
(84, 'ESC N° 24', NULL, NULL),
(85, 'ESC N° 25', NULL, NULL),
(86, 'ESC N° 27', NULL, NULL),
(87, 'ESC N° 3', NULL, NULL),
(88, 'ESC N° 43', NULL, NULL),
(89, 'ESC N° 45', NULL, NULL),
(90, 'ESC N° 5', NULL, NULL),
(91, 'ESC N° 501', NULL, NULL),
(92, 'ESC N° 6', NULL, NULL),
(93, 'ESC N° 66', NULL, NULL),
(94, 'ESC N° 7', NULL, NULL),
(95, 'ESC N° 8', NULL, NULL),
(96, 'ESC N°11', NULL, NULL),
(97, 'ESC N°17', NULL, NULL),
(98, 'ESC N°19', NULL, NULL),
(99, 'ESC N°3', NULL, NULL),
(100, 'ESC N°7', NULL, NULL),
(101, 'ESC de Arte', NULL, NULL),
(102, 'ESS N° 4', NULL, NULL),
(103, 'Enseñanza Media', NULL, NULL),
(104, 'Especial N° 502', NULL, NULL),
(105, 'Estrada', NULL, NULL),
(106, 'FACULTAD', NULL, NULL),
(107, 'INDUSTRIAL', NULL, NULL),
(108, 'Italiana', NULL, NULL),
(109, 'J 904', NULL, NULL),
(110, 'J. Manuel Strada', NULL, NULL),
(111, 'Jacarandá', NULL, NULL),
(112, 'Jardín Euforion', NULL, NULL),
(113, 'Jardín N° 903', NULL, NULL),
(114, 'Jardín N° 907', NULL, NULL),
(115, 'JoaquinV.Gonzalez', NULL, NULL),
(116, 'Lola Mora sec', NULL, NULL),
(117, 'Lujan Sierra', NULL, NULL),
(118, 'MUNICIOAL 11', NULL, NULL),
(119, 'María Auxiliadora', NULL, NULL),
(120, 'María Reina', NULL, NULL),
(121, 'Media 2 España', NULL, NULL),
(122, 'Media N 1', NULL, NULL),
(123, 'Mercedita de S.Martin', NULL, NULL),
(124, 'Monseñor Alberti', NULL, NULL),
(125, 'Mtro Luis MKEY', NULL, NULL),
(126, 'Mñor. Rasore', NULL, NULL),
(127, 'N1 Francisco', NULL, NULL),
(128, 'Normal 2', NULL, NULL),
(129, 'Normal 3 LP', NULL, NULL),
(130, 'Normal n 2', NULL, NULL),
(131, 'Ntra Sra Lourdes', NULL, NULL),
(132, 'Ntra. Sra. del Valle', NULL, NULL),
(133, 'PSICOLOGIA', NULL, NULL),
(134, 'Parroquial', NULL, NULL),
(135, 'Pasos del Libertedor', NULL, NULL),
(136, 'Ped 61', NULL, NULL),
(137, 'Pedagogica', NULL, NULL),
(138, 'SEC N° 8', NULL, NULL),
(139, 'SEC N°17', NULL, NULL),
(140, 'San Simón', NULL, NULL),
(141, 'Santa Rosa', NULL, NULL),
(142, 'Sra de Fátima', NULL, NULL),
(143, 'Sta Margarita', NULL, NULL),
(144, 'Sta Ro. de Lima', NULL, NULL),
(145, 'Sta Rosa', NULL, NULL),
(146, 'Sta Rosa Lima', NULL, NULL),
(147, 'Sta. R. de Lima', NULL, NULL),
(148, 'Sta. Rosa de lima', NULL, NULL),
(149, 'Técnica N° 1', NULL, NULL),
(150, 'Técnica N° 1 Berisso', NULL, NULL),
(151, 'Técnica N° 5', NULL, NULL),
(152, 'Técnica N° 7', NULL, NULL),
(153, 'UCALP', NULL, NULL),
(154, 'UNLP', NULL, NULL),
(155, 'UTN', NULL, NULL),
(156, 'Universitas', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `localidad_id` int(11) NOT NULL,
  `nivel_id` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genero_id` int(11) NOT NULL,
  `escuela_id` int(11) NOT NULL,
  `tipo_doc_id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `barrio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id`, `apellido`, `nombre`, `fecha_nac`, `localidad_id`, `nivel_id`, `domicilio`, `genero_id`, `escuela_id`, `tipo_doc_id`, `numero`, `tel`, `barrio_id`) VALUES
(39, 'Chaves', 'Andrés', '1990-01-01', 8, 1, '2456 dfghj', 1, 1, 1, 2468, '222222222', 1),
(40, 'Stanizani', 'Victor', '1960-02-02', 8, 5, '23 dfad', 1, 16, 1, 343434, '444554', 19),
(41, 'Fernández', 'Ignacio', '1980-10-10', 1, 2, '444 ssd', 1, 1, 1, 323232, '23456', 1),
(42, 'Zarza', 'Verónica', '1990-10-10', 8, 7, '2345 dff', 2, 17, 1, 2345, '4445543', 17),
(43, 'Chaves', 'Gonzalo', '1999-11-10', 1, 1, '233 aaa', 1, 1, 1, 23467, '44441', 1),
(44, 'Delgadillo', 'Cristian', '1999-11-11', 1, 2, '666 bsa', 3, 1, 1, 5556423, '2323', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante_taller`
--

CREATE TABLE `estudiante_taller` (
  `estudiante_id` int(11) NOT NULL,
  `taller_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante_taller`
--

INSERT INTO `estudiante_taller` (`estudiante_id`, `taller_id`) VALUES
(39, 13),
(40, 13),
(41, 13),
(42, 13),
(43, 14),
(44, 13);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `nombre`) VALUES
(1, 'Masculino'),
(2, 'Femenino'),
(3, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instrumento`
--

CREATE TABLE `instrumento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_id` int(11) NOT NULL,
  `codigo` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `imagen` varchar(500) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `instrumento`
--

INSERT INTO `instrumento` (`id`, `nombre`, `tipo_id`, `codigo`, `imagen`) VALUES
(6, 'Trompeta', 1, 'TROMP', 'no_image.jpeg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `log_clase`
--

CREATE TABLE `log_clase` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `clase_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `log_clase`
--

INSERT INTO `log_clase` (`id`, `fecha`, `clase_id`) VALUES
(20, '2019-12-11', 47),
(21, '2019-12-04', 47);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE `nivel` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `nivel`
--

INSERT INTO `nivel` (`id`, `nombre`) VALUES
(1, 'I'),
(2, 'II'),
(3, 'III'),
(4, 'IV'),
(5, 'V'),
(6, 'VI'),
(7, 'VII'),
(8, 'VIII'),
(9, 'IX'),
(10, 'X'),
(11, 'XI');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nucleo`
--

CREATE TABLE `nucleo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `latitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `longitud` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `nucleo`
--

INSERT INTO `nucleo` (`id`, `nombre`, `direccion`, `telefono`, `latitud`, `longitud`) VALUES
(1, 'nucleo 1', '12 y 54', '12321321', '-34.915905', '-57.953629'),
(2, 'nucleo 2', '13 y 55', '222222', '-34.911568', '-57.954981');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permiso`
--

CREATE TABLE `permiso` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `permiso`
--

INSERT INTO `permiso` (`id`, `nombre`) VALUES
(1, 'ELIMINAR_USUARIO'),
(2, 'CREAR_USUARIO'),
(3, 'MODIFICAR_USUARIO'),
(4, 'ACTIVAR_USUARIO'),
(5, 'LISTADO_USUARIOS'),
(6, 'CONFIGURACION'),
(7, 'VER_EN_MANTENIMIENTO'),
(8, 'LISTADO_DOCENTES'),
(9, 'LISTADO_ALUMNOS'),
(12, 'LISTADO_CICLOS'),
(13, 'LISTADO_TALLERES'),
(14, 'CREAR_TALLER'),
(15, 'CREAR_CICLO'),
(16, 'MODIFICAR_CICLO'),
(17, 'ELIMINAR_CICLO'),
(18, 'DETALLE_TALLER'),
(19, 'DETALLE_CICLO'),
(20, 'CREAR_ALUMNO'),
(21, 'MODIFICAR_ALUMNO'),
(22, 'ELIMINAR_ALUMNO'),
(23, 'DETALLE_ALUMNO'),
(24, 'CREAR_DOCENTE'),
(25, 'DETALLE_DOCENTE'),
(26, 'MODIFICAR_DOCENTE'),
(27, 'ELIMINAR_DOCENTE'),
(29, 'ELIMINAR_CLASE'),
(30, 'AGREGAR_EDITAR_CLASE'),
(31, 'VER_CLASES'),
(32, 'VER_ASISTENCIAS'),
(33, 'CREAR_ASISTENCIA'),
(34, 'LISTADO_INSTRUMENTOS'),
(35, 'DETALLE_INSTRUMENTO'),
(36, 'CREAR_INSTRUMENTO'),
(37, 'MODIFICAR_INSTRUMENTO'),
(38, 'ELIMINAR_INSTRUMENTO'),
(39, 'AGREGAR_DOCENTE_TALLER'),
(40, 'ELIMINAR_DOCENTE_TALLER'),
(41, 'ELIMINAR_ALUMNO_TALLER'),
(42, 'AGREGAR_ALUMNO_TALLER');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preceptor`
--

CREATE TABLE `preceptor` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preceptor_nucleo`
--

CREATE TABLE `preceptor_nucleo` (
  `preceptor_id` int(11) NOT NULL,
  `nucleo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsable`
--

CREATE TABLE `responsable` (
  `id` int(11) NOT NULL,
  `apellido` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `localidad_id` int(11) NOT NULL,
  `domicilio` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `genero_id` int(11) NOT NULL,
  `tipo_doc_id` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `tel` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `responsable`
--

INSERT INTO `responsable` (`id`, `apellido`, `nombre`, `fecha_nac`, `localidad_id`, `domicilio`, `genero_id`, `tipo_doc_id`, `numero`, `tel`) VALUES
(1, 'responsable', 'el', '2019-11-10', 1, 'asdsad', 1, 1, 12321321, '434232');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsable_estudiante`
--

CREATE TABLE `responsable_estudiante` (
  `responsable_id` int(11) NOT NULL,
  `estudiante_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `responsable_estudiante`
--

INSERT INTO `responsable_estudiante` (`responsable_id`, `estudiante_id`) VALUES
(1, 39),
(1, 40),
(1, 41),
(1, 42),
(1, 43),
(1, 44);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Docente'),
(3, 'Estudiante'),
(4, 'Preceptor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_tiene_permiso`
--

CREATE TABLE `rol_tiene_permiso` (
  `rol_id` int(11) NOT NULL,
  `permiso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rol_tiene_permiso`
--

INSERT INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
(0, 0),
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20),
(1, 21),
(1, 22),
(1, 23),
(1, 24),
(1, 25),
(1, 26),
(1, 27),
(1, 29),
(1, 30),
(1, 31),
(1, 32),
(1, 33),
(1, 34),
(1, 35),
(1, 36),
(1, 37),
(1, 38),
(1, 39),
(1, 40),
(1, 41),
(1, 42),
(2, 5),
(2, 8),
(2, 9),
(2, 12),
(2, 13),
(2, 18),
(2, 19),
(2, 21),
(2, 23),
(2, 25),
(2, 31),
(2, 32),
(2, 33),
(2, 34),
(2, 35),
(3, 5),
(3, 12),
(3, 13),
(3, 18),
(3, 19),
(3, 31),
(4, 8),
(4, 9),
(4, 12),
(4, 13),
(4, 18),
(4, 19),
(4, 21),
(4, 23),
(4, 25),
(4, 31),
(4, 32),
(4, 33),
(4, 34),
(4, 35),
(4, 39),
(4, 40),
(4, 41),
(4, 42);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `taller`
--

CREATE TABLE `taller` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_corto` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `nucleo_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `taller`
--

INSERT INTO `taller` (`id`, `nombre`, `nombre_corto`, `nucleo_id`) VALUES
(13, 'Coro', 'CORO', 1),
(14, 'Escritura musical', 'ESC', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_instrumento`
--

CREATE TABLE `tipo_instrumento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `tipo_instrumento`
--

INSERT INTO `tipo_instrumento` (`id`, `nombre`) VALUES
(1, 'Viento'),
(2, 'Cuerda'),
(3, 'Percusión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `email`, `username`, `password`, `activo`, `updated_at`, `created_at`, `first_name`, `last_name`) VALUES
(1, 'admin@mail.com', 'admin', '123', 1, '2019-11-07 19:15:27', '2019-10-23 00:00:00', 'admin', 'admin'),
(55, 'docente@mail.com', 'docente', '12345', 1, '2019-12-18 23:17:06', '2019-11-06 20:25:23', 'docente', 'prueba'),
(56, 'preceptor@mail.com', 'preceptor', '12345', 1, '2019-12-18 23:18:27', '2019-11-07 20:59:12', 'preceptor', 'prueba'),
(57, 'administrador@mail.com', 'administrador', '12345', 1, '2019-12-18 23:19:17', '2019-11-07 20:59:45', 'administrador', 'prueba'),
(59, 'estudiante@mail.com', 'estudiante', '12345', 1, '2019-12-18 23:17:40', '2019-11-07 21:00:30', 'estudiante', 'prueba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_tiene_rol`
--

CREATE TABLE `usuario_tiene_rol` (
  `usuario_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario_tiene_rol`
--

INSERT INTO `usuario_tiene_rol` (`usuario_id`, `rol_id`) VALUES
(1, 1),
(55, 2),
(56, 4),
(57, 1),
(59, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_asistencia_clase` (`clase_id`);

--
-- Indices de la tabla `barrio`
--
ALTER TABLE `barrio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ciclo_lectivo`
--
ALTER TABLE `ciclo_lectivo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clase`
--
ALTER TABLE `clase`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_clase_taller` (`taller_id`);

--
-- Indices de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `configuracion_sistema`
--
ALTER TABLE `configuracion_sistema`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_genero_docente_id` (`genero_id`);

--
-- Indices de la tabla `docente_clase`
--
ALTER TABLE `docente_clase`
  ADD PRIMARY KEY (`docente_id`,`clase_id`),
  ADD KEY `fk_docente_clase_clase` (`clase_id`);

--
-- Indices de la tabla `docente_taller`
--
ALTER TABLE `docente_taller`
  ADD PRIMARY KEY (`docente_id`,`taller_id`),
  ADD KEY `fk_docente_taller_taller` (`taller_id`);

--
-- Indices de la tabla `escuela`
--
ALTER TABLE `escuela`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_nivel_id` (`nivel_id`),
  ADD KEY `FK_genero_estudiante_id` (`genero_id`),
  ADD KEY `FK_escuela_id` (`escuela_id`),
  ADD KEY `FK_barrio_id` (`barrio_id`);

--
-- Indices de la tabla `estudiante_taller`
--
ALTER TABLE `estudiante_taller`
  ADD PRIMARY KEY (`estudiante_id`,`taller_id`),
  ADD KEY `fk_estudiante_taller_taller` (`taller_id`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `instrumento`
--
ALTER TABLE `instrumento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_tipo_instrumento_id` (`tipo_id`);

--
-- Indices de la tabla `log_clase`
--
ALTER TABLE `log_clase`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_log_clase_clase` (`clase_id`);

--
-- Indices de la tabla `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `nucleo`
--
ALTER TABLE `nucleo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permiso`
--
ALTER TABLE `permiso`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `preceptor`
--
ALTER TABLE `preceptor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `preceptor_nucleo`
--
ALTER TABLE `preceptor_nucleo`
  ADD PRIMARY KEY (`preceptor_id`,`nucleo_id`),
  ADD KEY `FK_nucleo_id` (`nucleo_id`);

--
-- Indices de la tabla `responsable`
--
ALTER TABLE `responsable`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_genero_responsable_id` (`genero_id`);

--
-- Indices de la tabla `responsable_estudiante`
--
ALTER TABLE `responsable_estudiante`
  ADD PRIMARY KEY (`responsable_id`,`estudiante_id`),
  ADD KEY `FK_estudiante_id` (`estudiante_id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol_tiene_permiso`
--
ALTER TABLE `rol_tiene_permiso`
  ADD PRIMARY KEY (`rol_id`,`permiso_id`);

--
-- Indices de la tabla `taller`
--
ALTER TABLE `taller`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_taller_nucleo` (`nucleo_id`);

--
-- Indices de la tabla `tipo_instrumento`
--
ALTER TABLE `tipo_instrumento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `usuario_tiene_rol`
--
ALTER TABLE `usuario_tiene_rol`
  ADD PRIMARY KEY (`usuario_id`,`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de la tabla `barrio`
--
ALTER TABLE `barrio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `ciclo_lectivo`
--
ALTER TABLE `ciclo_lectivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `clase`
--
ALTER TABLE `clase`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `configuracion`
--
ALTER TABLE `configuracion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `configuracion_sistema`
--
ALTER TABLE `configuracion_sistema`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `docente`
--
ALTER TABLE `docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `escuela`
--
ALTER TABLE `escuela`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=157;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `instrumento`
--
ALTER TABLE `instrumento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `log_clase`
--
ALTER TABLE `log_clase`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `nivel`
--
ALTER TABLE `nivel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `nucleo`
--
ALTER TABLE `nucleo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `permiso`
--
ALTER TABLE `permiso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `preceptor`
--
ALTER TABLE `preceptor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `responsable`
--
ALTER TABLE `responsable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `taller`
--
ALTER TABLE `taller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `tipo_instrumento`
--
ALTER TABLE `tipo_instrumento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD CONSTRAINT `fk_asistencia_clase` FOREIGN KEY (`clase_id`) REFERENCES `clase` (`id`);

--
-- Filtros para la tabla `clase`
--
ALTER TABLE `clase`
  ADD CONSTRAINT `fk_clase_taller` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Filtros para la tabla `docente`
--
ALTER TABLE `docente`
  ADD CONSTRAINT `FK_genero_docente_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`);

--
-- Filtros para la tabla `docente_clase`
--
ALTER TABLE `docente_clase`
  ADD CONSTRAINT `fk_docente_clase_clase` FOREIGN KEY (`clase_id`) REFERENCES `clase` (`id`),
  ADD CONSTRAINT `fk_docente_clase_docente` FOREIGN KEY (`docente_id`) REFERENCES `docente` (`id`);

--
-- Filtros para la tabla `docente_taller`
--
ALTER TABLE `docente_taller`
  ADD CONSTRAINT `fk_docente_taller_docente` FOREIGN KEY (`docente_id`) REFERENCES `docente` (`id`),
  ADD CONSTRAINT `fk_docente_taller_taller` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `FK_barrio_id` FOREIGN KEY (`barrio_id`) REFERENCES `barrio` (`id`),
  ADD CONSTRAINT `FK_escuela_id` FOREIGN KEY (`escuela_id`) REFERENCES `escuela` (`id`),
  ADD CONSTRAINT `FK_genero_estudiante_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`),
  ADD CONSTRAINT `FK_nivel_id` FOREIGN KEY (`nivel_id`) REFERENCES `nivel` (`id`);

--
-- Filtros para la tabla `estudiante_taller`
--
ALTER TABLE `estudiante_taller`
  ADD CONSTRAINT `fk_estudiante_taller_estudiante` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiante` (`id`),
  ADD CONSTRAINT `fk_estudiante_taller_taller` FOREIGN KEY (`taller_id`) REFERENCES `taller` (`id`);

--
-- Filtros para la tabla `instrumento`
--
ALTER TABLE `instrumento`
  ADD CONSTRAINT `FK_tipo_instrumento_id` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_instrumento` (`id`);

--
-- Filtros para la tabla `log_clase`
--
ALTER TABLE `log_clase`
  ADD CONSTRAINT `fk_log_clase_clase` FOREIGN KEY (`clase_id`) REFERENCES `clase` (`id`);

--
-- Filtros para la tabla `preceptor_nucleo`
--
ALTER TABLE `preceptor_nucleo`
  ADD CONSTRAINT `FK_nucleo_id` FOREIGN KEY (`nucleo_id`) REFERENCES `nucleo` (`id`),
  ADD CONSTRAINT `FK_preceptor_id` FOREIGN KEY (`preceptor_id`) REFERENCES `preceptor` (`id`);

--
-- Filtros para la tabla `responsable`
--
ALTER TABLE `responsable`
  ADD CONSTRAINT `FK_genero_responsable_id` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`);

--
-- Filtros para la tabla `responsable_estudiante`
--
ALTER TABLE `responsable_estudiante`
  ADD CONSTRAINT `FK_estudiante_id` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiante` (`id`),
  ADD CONSTRAINT `FK_responsable_id` FOREIGN KEY (`responsable_id`) REFERENCES `responsable` (`id`);

--
-- Filtros para la tabla `taller`
--
ALTER TABLE `taller`
  ADD CONSTRAINT `fk_taller_nucleo` FOREIGN KEY (`nucleo_id`) REFERENCES `nucleo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
