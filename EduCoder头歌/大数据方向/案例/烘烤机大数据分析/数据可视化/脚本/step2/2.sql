/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : roaster

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 21/04/2021 18:15:36
*/
DROP database IF EXISTS mydb;
CREATE database IF not EXISTS mydb;
use mydb;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for year_avg_quality
-- ----------------------------
DROP TABLE IF EXISTS `year_avg_quality`;
CREATE TABLE `year_avg_quality`  (
  `year` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avg_quality` double NULL DEFAULT NULL,
  PRIMARY KEY (`year`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of year_avg_quality
-- ----------------------------
INSERT INTO `year_avg_quality` VALUES ('2015', 403.41);
INSERT INTO `year_avg_quality` VALUES ('2016', 401.05);
INSERT INTO `year_avg_quality` VALUES ('2017', 404.55);
INSERT INTO `year_avg_quality` VALUES ('2018', 403.95);
INSERT INTO `year_avg_quality` VALUES ('2019', 366.95);

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------
-- Table structure for year_avg_roaster
-- ----------------------------
DROP TABLE IF EXISTS `year_avg_roaster`;
CREATE TABLE `year_avg_roaster`  (
  `year` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avg_T` double NULL DEFAULT NULL,
  `avg_H` double NULL DEFAULT NULL,
  `avg_AH` double NULL DEFAULT NULL,
  PRIMARY KEY (`year`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of year_avg_roaster
-- ----------------------------
INSERT INTO `year_avg_roaster` VALUES ('2015', 340.04, 174.63, 7.5);
INSERT INTO `year_avg_roaster` VALUES ('2016', 340.54, 174.46, 7.51);
INSERT INTO `year_avg_roaster` VALUES ('2017', 339.28, 175.07, 7.5);
INSERT INTO `year_avg_roaster` VALUES ('2018', 340.47, 174.71, 7.49);
INSERT INTO `year_avg_roaster` VALUES ('2019', 339.8, 159.73, 7.35);

SET FOREIGN_KEY_CHECKS = 1;
