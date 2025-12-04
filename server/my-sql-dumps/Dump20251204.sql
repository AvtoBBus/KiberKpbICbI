CREATE DATABASE  IF NOT EXISTS `newschema` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `newschema`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: newschema
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food` (
  `FoodID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `CategoryID` int NOT NULL,
  `Calories` int unsigned NOT NULL,
  `Protein` int unsigned NOT NULL,
  `Fats` int unsigned NOT NULL,
  `Carbonates` int unsigned NOT NULL,
  PRIMARY KEY (`FoodID`),
  KEY `CategoryID_idx` (`CategoryID`),
  CONSTRAINT `foodCategoryID` FOREIGN KEY (`CategoryID`) REFERENCES `foodcategories` (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (1,'Куриная грудка',3,165,31,3,0),(2,'Гречневая каша',6,132,4,1,27),(3,'Яблоки',2,52,0,0,14),(4,'Огурцы',1,15,1,0,3),(5,'Творог 5%',5,121,17,5,3),(6,'Лосось',4,208,20,13,0),(7,'Молоко 2.5%',5,52,3,2,5),(8,'Рис вареный',6,130,3,0,28),(9,'Бананы',2,89,1,0,23),(10,'Помидоры',1,18,1,0,4),(13,'TEST',3,555,555,555,555),(14,'Куриная попа',1,222,222,222,333),(16,'Копыто единорога',3,222,222,222,222);
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foodcategories`
--

DROP TABLE IF EXISTS `foodcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foodcategories` (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(45) NOT NULL,
  PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foodcategories`
--

LOCK TABLES `foodcategories` WRITE;
/*!40000 ALTER TABLE `foodcategories` DISABLE KEYS */;
INSERT INTO `foodcategories` VALUES (1,'Овощи'),(2,'Фрукты'),(3,'Мясо'),(4,'Рыба'),(5,'Молочные продукты'),(6,'Крупы'),(7,'Напитки');
/*!40000 ALTER TABLE `foodcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foodinmeal`
--

DROP TABLE IF EXISTS `foodinmeal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foodinmeal` (
  `FoodInMealID` int NOT NULL AUTO_INCREMENT,
  `MealID` int NOT NULL,
  `ProductID` int NOT NULL,
  `ProductName` varchar(45) NOT NULL,
  `Calories` int NOT NULL,
  `Protein` int NOT NULL,
  `Fats` int NOT NULL,
  `Carbonates` int NOT NULL,
  PRIMARY KEY (`FoodInMealID`),
  KEY `foodinmealMeakID_idx` (`MealID`),
  CONSTRAINT `foodinmealMealID` FOREIGN KEY (`MealID`) REFERENCES `meal` (`MealID`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foodinmeal`
--

LOCK TABLES `foodinmeal` WRITE;
/*!40000 ALTER TABLE `foodinmeal` DISABLE KEYS */;
INSERT INTO `foodinmeal` VALUES (4,2,1,'food',0,0,0,0),(5,2,8,'food',0,0,0,0),(6,2,4,'food',0,0,0,0),(7,3,6,'food',0,0,0,0),(8,3,2,'food',0,0,0,0),(9,3,9,'food',0,0,0,0),(13,5,1,'food',0,0,0,0),(14,5,2,'food',0,0,0,0),(15,5,10,'food',0,0,0,0),(16,6,5,'food',0,0,0,0),(17,6,9,'food',0,0,0,0),(18,7,2,'food',0,0,0,0),(19,7,1,'food',0,0,0,0),(20,7,7,'food',0,0,0,0),(21,8,6,'food',0,0,0,0),(22,8,8,'food',0,0,0,0),(23,8,4,'food',0,0,0,0),(24,9,5,'food',0,0,0,0),(25,9,3,'food',0,0,0,0),(26,9,10,'food',0,0,0,0),(29,14,2,'food',0,0,0,0),(39,1,0,'food1',1,1,1,1),(42,22,1,'food',0,0,0,0),(43,23,2,'food',0,0,0,0),(44,23,3,'food',0,0,0,0),(48,25,2,'food',0,0,0,0),(49,1,1,'food2',2,2,2,2),(50,1,2,'food3',3,3,3,3),(54,35,1,'food3',3,3,3,3),(55,37,0,'food4',4,4,4,4),(56,38,0,'хурма',120,1,0,31),(57,39,0,'хурма',120,1,0,31),(58,40,1,'food1',1,1,1,1),(59,41,2,'food2',2,2,2,2),(60,42,3,'food3',3,3,3,3),(70,4,0,'1',1,1,1,1),(71,4,1,'2',2,2,2,2),(72,40,1,'еда',400,7,20,45),(73,43,0,'2',2,2,2,2),(74,41,1,'пирог',400,8,20,40),(75,41,2,'хурма',120,1,0,31),(76,41,3,'о',450,8,20,40),(77,44,0,'ж',450,8,15,40);
/*!40000 ALTER TABLE `foodinmeal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meal`
--

DROP TABLE IF EXISTS `meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meal` (
  `MealID` int NOT NULL AUTO_INCREMENT,
  `Date` datetime NOT NULL,
  `MealType` int NOT NULL DEFAULT '1',
  `UserID` int NOT NULL,
  PRIMARY KEY (`MealID`),
  KEY `UserID_idx` (`UserID`),
  CONSTRAINT `mealUserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meal`
--

LOCK TABLES `meal` WRITE;
/*!40000 ALTER TABLE `meal` DISABLE KEYS */;
INSERT INTO `meal` VALUES (1,'2024-01-15 09:00:00',1,1),(2,'2024-01-15 14:00:00',2,1),(3,'2024-01-15 19:00:00',3,1),(4,'2024-01-15 00:00:00',1,2),(5,'2024-01-15 00:00:00',2,2),(6,'2024-01-15 00:00:00',3,2),(7,'2024-01-15 07:45:00',1,3),(8,'2024-01-15 13:15:00',2,3),(9,'2024-01-15 19:30:00',3,3),(14,'2024-01-15 22:00:00',1,1),(22,'2025-11-19 06:51:33',2,1),(23,'2025-11-19 06:51:33',3,1),(25,'2026-01-20 05:09:47',1,1),(35,'2027-01-15 00:00:00',1,1),(37,'2027-01-15 00:00:00',2,1),(38,'2025-11-23 00:00:00',3,38),(39,'2025-11-25 00:00:00',1,38),(40,'2025-11-26 00:00:00',1,38),(41,'2025-11-26 00:00:00',2,38),(42,'2025-11-26 00:00:00',3,38),(43,'2024-01-16 00:00:00',1,2),(44,'2025-11-27 00:00:00',2,38);
/*!40000 ALTER TABLE `meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normcpfc`
--

DROP TABLE IF EXISTS `normcpfc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normcpfc` (
  `NormID` int NOT NULL AUTO_INCREMENT,
  `Weight` int unsigned NOT NULL,
  `Height` int NOT NULL,
  `DesiredWeight` int NOT NULL,
  `Calories` int unsigned NOT NULL,
  `Protein` int unsigned NOT NULL,
  `Fats` int unsigned NOT NULL,
  `Carbonatest` int unsigned NOT NULL,
  `UserID` int NOT NULL,
  PRIMARY KEY (`NormID`),
  KEY `UserID_idx` (`UserID`),
  CONSTRAINT `UserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normcpfc`
--

LOCK TABLES `normcpfc` WRITE;
/*!40000 ALTER TABLE `normcpfc` DISABLE KEYS */;
INSERT INTO `normcpfc` VALUES (2,0,0,0,0,0,0,0,2),(3,0,0,0,0,0,0,0,3),(4,0,0,0,0,0,0,0,4),(5,0,0,0,0,0,0,0,5),(6,0,0,0,0,0,0,0,6),(7,0,0,0,0,0,0,0,7),(14,58,183,65,2670,167,74,334,1),(15,100,190,90,2434,152,68,304,38);
/*!40000 ALTER TABLE `normcpfc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statisticcpfc`
--

DROP TABLE IF EXISTS `statisticcpfc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statisticcpfc` (
  `StatisticCPFCID` int NOT NULL AUTO_INCREMENT,
  `Date` datetime NOT NULL,
  `Calories` int NOT NULL,
  `Protein` int NOT NULL,
  `Fats` int NOT NULL,
  `Carbonates` int NOT NULL,
  `UserID` int NOT NULL,
  PRIMARY KEY (`StatisticCPFCID`),
  KEY `UserID_idx` (`UserID`),
  CONSTRAINT `statisticcpfcUserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statisticcpfc`
--

LOCK TABLES `statisticcpfc` WRITE;
/*!40000 ALTER TABLE `statisticcpfc` DISABLE KEYS */;
INSERT INTO `statisticcpfc` VALUES (1,'2024-01-15 08:00:00',1111,1111,1111,1111,1),(2,'2024-01-15 14:00:00',2380,130,62,285,1),(5,'2024-01-15 00:00:00',2850,145,75,320,3),(6,'2024-01-16 00:00:00',2780,140,72,315,3),(7,'2024-01-15 00:00:00',2150,105,60,265,4),(8,'2024-01-16 00:00:00',2200,110,62,270,4),(9,'2024-01-15 19:00:00',1,1,1,1,1),(14,'2025-11-22 00:00:00',1,1,1,1,38),(15,'2025-11-22 00:00:00',2,2,2,2,38),(16,'2025-11-22 00:00:00',3,3,3,3,38),(21,'2024-01-15 00:00:00',3,3,3,3,2),(22,'2025-11-26 00:00:00',1370,24,60,156,38),(23,'2024-01-16 00:00:00',2,2,2,2,2),(24,'2025-11-27 00:00:00',450,8,15,40,38);
/*!40000 ALTER TABLE `statisticcpfc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statisticwh`
--

DROP TABLE IF EXISTS `statisticwh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statisticwh` (
  `StatisticWHID` int NOT NULL AUTO_INCREMENT,
  `Date` datetime NOT NULL,
  `Height` int NOT NULL,
  `Weight` int NOT NULL,
  `UserID` int NOT NULL,
  PRIMARY KEY (`StatisticWHID`),
  KEY `UserID_idx` (`UserID`),
  CONSTRAINT `statisticwhUserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statisticwh`
--

LOCK TABLES `statisticwh` WRITE;
/*!40000 ALTER TABLE `statisticwh` DISABLE KEYS */;
INSERT INTO `statisticwh` VALUES (1,'2023-01-15 00:00:00',1,1,1),(2,'2024-01-15 00:00:00',2,2,1),(3,'2024-01-15 00:00:00',3,3,1),(4,'2024-01-15 00:00:00',4,4,2),(5,'2024-01-15 00:00:00',5,5,2),(6,'2024-01-15 00:00:00',177,72,1),(7,'2024-01-16 00:00:00',177,71,1),(9,'2024-01-16 00:00:00',168,62,2),(10,'2024-01-16 00:00:00',168,61,2),(11,'2024-01-16 00:00:00',168,60,2),(12,'2024-01-16 00:00:00',182,82,3),(13,'2024-01-16 00:00:00',182,83,3),(14,'2024-01-16 00:00:00',182,84,3),(15,'2024-01-16 00:00:00',172,67,4),(16,'2024-01-16 00:00:00',172,66,4),(17,'2024-01-16 00:00:00',172,65,4),(18,'2024-02-15 00:00:00',123,321,1),(19,'2025-11-22 00:00:00',1,1,38),(20,'2025-11-22 00:00:00',2,2,38),(21,'2025-11-22 00:00:00',3,3,38);
/*!40000 ALTER TABLE `statisticwh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Salt` mediumtext NOT NULL,
  `Password` mediumtext NOT NULL,
  `Email` varchar(512) NOT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `AccessToken` mediumtext,
  `RefreshToken` mediumtext,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Phone_UNIQUE` (`Phone`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','test@test.com','12345678900','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjEsIkVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIlBob25lIjoiMTIzNDU2Nzg5MDAiLCJleHAiOjIzNjQxNjY5ODZ9.paBuJFNUKC81_evku65b6hZfd9PGNfJ99wEgovhiDfc','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjEsIkVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIlBob25lIjoiMTIzNDU2Nzg5MDAiLCJleHAiOjE3NjQyNTM0NDZ9.-2DDrdqYPooZ5ltTNtl7T3jcsUmAo9Ja2mV6qiNP_to'),(2,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','22@22.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjIsIkVtYWlsIjoiMjJAMjIuY29tIiwiUGhvbmUiOm51bGwsImV4cCI6MjM2NDE1NTQ4NH0.S_lpFYbll1nbF4Q04yhDjTbyFpgPs_oRK9FtTfGViu4','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjIsIkVtYWlsIjoiMjJAMjIuY29tIiwiUGhvbmUiOm51bGwsImV4cCI6MTc2NDI0MTk0NH0.L0xZWx_lfKtxQKa2-iD78pa7ag0QJXUNjSsL4JLEQOc'),(3,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','ivan@mail.ru','+79161234567',NULL,NULL),(4,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','maria@mail.ru','+79167654321',NULL,NULL),(5,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','alex@mail.ru','+79169998877',NULL,NULL),(6,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','olga@mail.ru','+79165554433',NULL,NULL),(7,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','dmitry@mail.ru','+79163332211',NULL,NULL),(9,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','aboba@example.com','string',NULL,NULL),(10,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','normis@example.com','normis',NULL,NULL),(29,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','auth_test@example.com','auth_test',NULL,NULL),(30,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','zxczxczxc@zxczxczxczcx.com',NULL,NULL,NULL),(31,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','q@q.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjMxLCJFbWFpbCI6InFAcS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMjA0MTczfQ.K9DDs_bxbFKIZmhO8XeNwM9ZsyRsfZJBZxHsLV8Ukkg','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjMxLCJFbWFpbCI6InFAcS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMjkwMjczfQ.5dLpMLhFqb8CvqBg-c0o3bkqGQqFuOX86dvg5BXZShw'),(32,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','a@a.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjMyLCJFbWFpbCI6ImFAYS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzAwMjI1fQ.9xBCqbuxgZ49-pz8dcSxigC6QQWCvzQl2x5tpcs1Ato','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjMyLCJFbWFpbCI6ImFAYS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzg2MzI1fQ.GR0lxyWunNJaOR1Bed39imcNUr0qtT0jSMXLMGv3VkA'),(34,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','d@d.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM0LCJFbWFpbCI6ImRAZC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzA2NTQwfQ.clEQ6-zsDVct3xkWWLSSv0RhPZ5xzn1eN8n2gOUlrEM','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM0LCJFbWFpbCI6ImRAZC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzkyNjQwfQ.LHnGZVSnqvTwQ4Gdu1anJc6JJa86O3b3C9b22ieDWlY'),(35,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','d@xxxd.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM1LCJFbWFpbCI6ImRAeHh4ZC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzA2Njg0fQ.XQp4ombeXx4CgefNhDHv4JUreODjja1RpbZDn3EmznY','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM1LCJFbWFpbCI6ImRAeHh4ZC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzkyNzg0fQ.ARaDoWG88PCW7EvFnsB1eXTTRHzbUhl5UTye7JUqJ6g'),(36,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','m@m.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM2LCJFbWFpbCI6Im1AbS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzA2ODc3fQ.-G9GcvtE64B48fRJty-UTJzo_clkeIBaG9d2TuULG3c','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM2LCJFbWFpbCI6Im1AbS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzkyOTc3fQ.v4PhRAqWyNv2ErQIIP0PYrgIOK1zQbyfrukn4IL6l_Q'),(37,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','n@n.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM3LCJFbWFpbCI6Im5Abi5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzA2OTIwfQ.wAMqVmL0eqhtmRgLpnpsTD3SY6yhC5YD8_raPrHiUpE','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM3LCJFbWFpbCI6Im5Abi5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzkzMDIwfQ.rSMiszEpORimQX7Al-oqOo-KukOhDfYFqaZWYu2hxOk'),(38,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','w@w.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM4LCJFbWFpbCI6IndAdy5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoyMzY0MTc2NzgwfQ.Y8bO5GjGqTTc2U7JIoATzzRT_QfmILHNx5o8STs1ggE','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM4LCJFbWFpbCI6IndAdy5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzY0MjYzMjQwfQ.Oi15gclaFUDKAnphZ0uQrMQnvvl7H9qI6oH3-fBOKno'),(39,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','p@p.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM5LCJFbWFpbCI6InBAcC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzMzIwOTE1fQ.zJcnFJJS7EsdUwv4_3InbpE7CsKwcerCSaDyHBu4NKU','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjM5LCJFbWFpbCI6InBAcC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzNDA3MDE1fQ.eoRrpN_VhxwG6OcrefZKzZ3YbZdI4PL8pqlUlUOpobU'),(40,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','k@k.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQwLCJFbWFpbCI6ImtAay5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzNDAyNjQyfQ.JMe5uoTmmnsNLtIWhHH93PilNAuP8GYUytOQpRHwu84','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQwLCJFbWFpbCI6ImtAay5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzNDg4NzQyfQ.eIW3oeL84jk2aOamN0KWCXaHR0b40zjy9v48OJMqARQ'),(42,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c','zzz@zzzz.com',NULL,NULL,NULL),(43,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','e@e.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQzLCJFbWFpbCI6ImVAZS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoyMzYzNTYwMjI5fQ.I69gNp0kVKSGhgv793BEPKgzrj4el-oy3pkyIkhOgt0','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQzLCJFbWFpbCI6ImVAZS5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzNjQ2Njg5fQ.OMV8dAJLzZH4uYtn2lIOWKRbmqs2Q2UZaG752xC7FrE'),(44,'2d8858de207c2d24ba47dec72cf2637ad68c367f81d35d37f84fe540f9bcebdf','6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b','t@t.com',NULL,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQ0LCJFbWFpbCI6InRAdC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoyMzYzNTYyNjEyfQ.CNaS8g3hyjW5ojtnx4Eem_6dW3Be8axni-ew932xs9o','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOjQ0LCJFbWFpbCI6InRAdC5jb20iLCJQaG9uZSI6bnVsbCwiZXhwIjoxNzYzNjQ5MDcyfQ.7wqOO93NKbP4eCPYHUy42B_HZJJeF8a2PS_uWw57-4o');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdata` (
  `UserDataID` int NOT NULL AUTO_INCREMENT,
  `UserName` varchar(45) NOT NULL,
  `Height` int NOT NULL,
  `Weight` int NOT NULL,
  `Age` int NOT NULL,
  `DesiredHeight` int NOT NULL,
  `DesiredWeight` int NOT NULL,
  `Activity` int NOT NULL,
  `UserID` int NOT NULL,
  `Gender` enum('м','ж') NOT NULL DEFAULT 'м',
  PRIMARY KEY (`UserDataID`),
  KEY `userdataUserID_idx` (`UserID`),
  CONSTRAINT `userdataUserID` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES (4,'4',168,62,30,0,0,0,2,'м'),(5,'5',182,82,28,0,0,0,3,'м'),(6,'6',172,67,35,0,0,0,4,'м'),(7,'7',162,57,22,0,0,0,5,'м'),(11,'woooof',190,100,26,190,90,3,38,'м'),(12,'тест',5,5,5,5,5,1,39,'м'),(13,'Крутой тип 228',222,222,22,223,223,2,1,'м'),(14,'о',150,50,15,150,48,0,43,'ж'),(15,'о',170,70,25,170,65,3,44,'ж');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usergoal`
--

DROP TABLE IF EXISTS `usergoal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usergoal` (
  `GoalID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Description` mediumtext,
  `UserID` int NOT NULL,
  PRIMARY KEY (`GoalID`),
  KEY `UserID_idx` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usergoal`
--

LOCK TABLES `usergoal` WRITE;
/*!40000 ALTER TABLE `usergoal` DISABLE KEYS */;
INSERT INTO `usergoal` VALUES (1,'123','aboba',1),(2,'123','aboabobaoabbao',1),(3,'321','2221231233',2);
/*!40000 ALTER TABLE `usergoal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `userstatistic`
--

DROP TABLE IF EXISTS `userstatistic`;
/*!50001 DROP VIEW IF EXISTS `userstatistic`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `userstatistic` AS SELECT 
 1 AS `ID`,
 1 AS `UserID`,
 1 AS `Date`,
 1 AS `UserHeight`,
 1 AS `UserWeight`,
 1 AS `Calories`,
 1 AS `Protein`,
 1 AS `Fats`,
 1 AS `Carbonates`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'newschema'
--

--
-- Final view structure for view `userstatistic`
--

/*!50001 DROP VIEW IF EXISTS `userstatistic`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=TEMPTABLE */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `userstatistic` AS select row_number() OVER (ORDER BY `t1`.`UserID`,`t2`.`Date` )  AS `ID`,`t1`.`UserID` AS `UserID`,`t2`.`Date` AS `Date`,`t2`.`Height` AS `UserHeight`,`t2`.`Weight` AS `UserWeight`,`t3`.`Calories` AS `Calories`,`t3`.`Protein` AS `Protein`,`t3`.`Fats` AS `Fats`,`t3`.`Carbonates` AS `Carbonates` from ((`user` `t1` left join `statisticwh` `t2` on((`t1`.`UserID` = `t2`.`UserID`))) left join `statisticcpfc` `t3` on(((`t1`.`UserID` = `t3`.`UserID`) and (`t2`.`Date` = `t3`.`Date`)))) where ((`t1`.`UserID` is not null) and (`t2`.`Date` is not null) and (`t2`.`Height` is not null) and (`t2`.`Weight` is not null) and (`t3`.`Calories` is not null) and (`t3`.`Protein` is not null) and (`t3`.`Fats` is not null) and (`t3`.`Carbonates` is not null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-04 12:57:57
