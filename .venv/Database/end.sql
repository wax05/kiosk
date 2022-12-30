-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.9.2-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- kiosk 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `kiosk` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_bin */;
USE `kiosk`;

-- 테이블 kiosk.admin_data 구조 내보내기
CREATE TABLE IF NOT EXISTS `admin_data` (
  `user_id` varchar(13) DEFAULT NULL,
  `pw_hash` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='admin Data';

-- 테이블 데이터 kiosk.admin_data:~1 rows (대략적) 내보내기
DELETE FROM `admin_data`;
/*!40000 ALTER TABLE `admin_data` DISABLE KEYS */;
INSERT INTO `admin_data` (`user_id`, `pw_hash`) VALUES
	('admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
/*!40000 ALTER TABLE `admin_data` ENABLE KEYS */;

-- 테이블 kiosk.get_code 구조 내보내기
CREATE TABLE IF NOT EXISTS `get_code` (
  `Code` varchar(5) COLLATE utf8mb3_bin NOT NULL,
  `ProductCode` varchar(15) COLLATE utf8mb3_bin DEFAULT NULL,
  `used` int(11) DEFAULT NULL,
  `get` int(11) DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.get_code:~0 rows (대략적) 내보내기
DELETE FROM `get_code`;
/*!40000 ALTER TABLE `get_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `get_code` ENABLE KEYS */;

-- 테이블 kiosk.product_code 구조 내보내기
CREATE TABLE IF NOT EXISTS `product_code` (
  `ProductCode` varchar(20) COLLATE utf8mb3_bin NOT NULL,
  `ProductName` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`ProductCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.product_code:~0 rows (대략적) 내보내기
DELETE FROM `product_code`;
/*!40000 ALTER TABLE `product_code` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_code` ENABLE KEYS */;

-- 테이블 kiosk.take 구조 내보내기
CREATE TABLE IF NOT EXISTS `take` (
  `Code` varchar(10) COLLATE utf8mb3_bin NOT NULL,
  `Take` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  `Time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;

-- 테이블 데이터 kiosk.take:~0 rows (대략적) 내보내기
DELETE FROM `take`;
/*!40000 ALTER TABLE `take` DISABLE KEYS */;
/*!40000 ALTER TABLE `take` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
