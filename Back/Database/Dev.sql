-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.8.3-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- kiosk 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `kiosk` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_bin */;
USE `kiosk`;

-- 테이블 kiosk.cli_key 구조 내보내기
CREATE TABLE IF NOT EXISTS `cli_key` (
  `API_KEY` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.cli_key:~40 rows (대략적) 내보내기
INSERT INTO `cli_key` (`API_KEY`) VALUES
	('7a71500ea07b4a29fc70'),
	('cacf8c7d825c76c9db5c'),
	('46d0a25634880efbed23'),
	('a33b8116c6cd81fde0f9'),
	('55f4d9db6a763ec933a8'),
	('87df2f73dc390bf4ee60'),
	('d2885c993a545b669756'),
	('cc58313da65f51ce140d'),
	('2de5efb00c26f8c89bba'),
	('f57ef679d72d9464d371'),
	('4498835d790b7e7da875'),
	('6b195c71ec312676e555'),
	('ac2d1065f43c3286151d'),
	('48d2c822b9630213bfbe'),
	('674ed6bb6603cbeb8edc'),
	('e64c9d3be7247877da7f'),
	('18e14ef4916f9b4f0f63'),
	('a36ceccde7e884ae0b07'),
	('ec03d7bdaef58c84009a'),
	('508c1ccbc66a28465493'),
	('adc791f78ad3b740f79e'),
	('b7fe281358da5e382688'),
	('59a54282c2f05c76e556'),
	('3b70ce607d40fce5afed'),
	('d6486e92f1e1f2fb54bd'),
	('8eb0e6a02cff1462b149'),
	('378d38793d027d6b23b0'),
	('f250e64cafcbc0012fae'),
	('bc5ade169a3f546adf0d'),
	('eb0abe28b1691c4a5621'),
	('4e49a285e130e5a31901'),
	('a9706d0cf2511771020a'),
	('c2a8cb5dcb6332aa5fa2'),
	('d1d117fc97309a579fdf'),
	('a7b0833eb9c8e613e972'),
	('7f576212c6b6642021b0'),
	('87a04472a93de6866672'),
	('c183e266089fa1d02ee0'),
	('5b52a255208eea5a6fb5'),
	('f8aeb04caf0e5287f413'),
	('asdf');

-- 테이블 kiosk.code 구조 내보내기
CREATE TABLE IF NOT EXISTS `code` (
  `code` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  `product_code` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  `take` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  `used` tinyint(4) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.code:~2 rows (대략적) 내보내기
INSERT INTO `code` (`code`, `product_code`, `take`, `used`) VALUES
	('12345', 'Test1', 'admin', 1),
	('qwert', 'qwer', '', 0);

-- 테이블 kiosk.product 구조 내보내기
CREATE TABLE IF NOT EXISTS `product` (
  `code` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL,
  `name` varchar(50) COLLATE utf8mb3_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.product:~6 rows (대략적) 내보내기
INSERT INTO `product` (`code`, `name`) VALUES
	('Test1', '인형'),
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('4', '4');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
