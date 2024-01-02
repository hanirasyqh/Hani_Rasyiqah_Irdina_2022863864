-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2024 at 03:36 PM
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
CREATE DATABASE IF NOT EXISTS student_marks;
USE student_marks;
--

-- --------------------------------------------------------

--
-- Table structure for table `stud_score`
--

CREATE TABLE `stud_score` (
  `stud_name` varchar(11) DEFAULT NULL,
  `math_score` int(3) NOT NULL,
  `english_score` int(3) NOT NULL,
  `history_score` int(3) NOT NULL,
  `total_marks` int(3) NOT NULL,
  `average` int(10) NOT NULL,
  `grade` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stud_score`
--

INSERT INTO `stud_score` (`stud_name`, `math_score`, `english_score`, `history_score`, `total_marks`, `average`, `grade`) VALUES
('hani', 56, 88, 86, 0, 0, ''),
('ira', 78, 88, 57, 223, 74, 'pass!'),
('yani', 65, 46, 66, 177, 59, 'pass!'),
('idan', 46, 97, 57, 200, 67, 'pass!'),
('mama', 100, 90, 70, 260, 87, 'pass!'),
('eyam', 30, 46, 54, 130, 43, 'fail'),
('dina', 79, 78, 68, 225, 75, 'pass!'),
('izs', 24, 43, 40, 107, 36, 'fail'),
('peah', 25, 67, 45, 137, 46, 'fail'),
('Aleen', 46, 34, 43, 123, 41, 'fail'),
('bubu', 78, 98, 68, 244, 81, 'pass!');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
