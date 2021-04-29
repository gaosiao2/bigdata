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

 Date: 20/04/2021 16:28:02
*/
DROP database IF EXISTS mydb;
CREATE database IF not EXISTS mydb;
use mydb;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `month_avg_quality`;
CREATE TABLE `month_avg_quality`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `years` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `months` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `avg_quality` double NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of month_avg_quality
-- ----------------------------
INSERT INTO `month_avg_quality` VALUES (1, '2015', '01', 403.5);
INSERT INTO `month_avg_quality` VALUES (2, '2015', '02', 403.12);
INSERT INTO `month_avg_quality` VALUES (3, '2015', '03', 402.06);
INSERT INTO `month_avg_quality` VALUES (4, '2015', '04', 406.65);
INSERT INTO `month_avg_quality` VALUES (5, '2015', '05', 406.57);
INSERT INTO `month_avg_quality` VALUES (6, '2015', '06', 402.6);
INSERT INTO `month_avg_quality` VALUES (7, '2015', '07', 401.58);
INSERT INTO `month_avg_quality` VALUES (8, '2015', '08', 407.64);
INSERT INTO `month_avg_quality` VALUES (9, '2015', '09', 403.58);
INSERT INTO `month_avg_quality` VALUES (10, '2015', '10', 403.46);
INSERT INTO `month_avg_quality` VALUES (11, '2015', '11', 409.53);
INSERT INTO `month_avg_quality` VALUES (12, '2015', '12', 390.32);
INSERT INTO `month_avg_quality` VALUES (13, '2016', '01', 394.24);
INSERT INTO `month_avg_quality` VALUES (14, '2016', '02', 403.99);
INSERT INTO `month_avg_quality` VALUES (15, '2016', '03', 404.38);
INSERT INTO `month_avg_quality` VALUES (16, '2016', '04', 401.11);
INSERT INTO `month_avg_quality` VALUES (17, '2016', '05', 398.3);
INSERT INTO `month_avg_quality` VALUES (18, '2016', '06', 390.81);
INSERT INTO `month_avg_quality` VALUES (19, '2016', '07', 404.06);
INSERT INTO `month_avg_quality` VALUES (20, '2016', '08', 392.57);
INSERT INTO `month_avg_quality` VALUES (21, '2016', '09', 413.57);
INSERT INTO `month_avg_quality` VALUES (22, '2016', '10', 406.38);
INSERT INTO `month_avg_quality` VALUES (23, '2016', '11', 406.29);
INSERT INTO `month_avg_quality` VALUES (24, '2016', '12', 397.34);
INSERT INTO `month_avg_quality` VALUES (25, '2017', '01', 409.3);
INSERT INTO `month_avg_quality` VALUES (26, '2017', '02', 420.93);
INSERT INTO `month_avg_quality` VALUES (27, '2017', '03', 402.41);
INSERT INTO `month_avg_quality` VALUES (28, '2017', '04', 406.38);
INSERT INTO `month_avg_quality` VALUES (29, '2017', '05', 417.48);
INSERT INTO `month_avg_quality` VALUES (30, '2017', '06', 398.62);
INSERT INTO `month_avg_quality` VALUES (31, '2017', '07', 396.7);
INSERT INTO `month_avg_quality` VALUES (32, '2017', '08', 402.27);
INSERT INTO `month_avg_quality` VALUES (33, '2017', '09', 402.99);
INSERT INTO `month_avg_quality` VALUES (34, '2017', '10', 392.81);
INSERT INTO `month_avg_quality` VALUES (35, '2017', '11', 404.61);
INSERT INTO `month_avg_quality` VALUES (36, '2017', '12', 401.5);
INSERT INTO `month_avg_quality` VALUES (37, '2018', '01', 403.5);
INSERT INTO `month_avg_quality` VALUES (38, '2018', '02', 403.12);
INSERT INTO `month_avg_quality` VALUES (39, '2018', '03', 403.69);
INSERT INTO `month_avg_quality` VALUES (40, '2018', '04', 406.92);
INSERT INTO `month_avg_quality` VALUES (41, '2018', '05', 406.57);
INSERT INTO `month_avg_quality` VALUES (42, '2018', '06', 403.26);
INSERT INTO `month_avg_quality` VALUES (43, '2018', '07', 401.58);
INSERT INTO `month_avg_quality` VALUES (44, '2018', '08', 407.64);
INSERT INTO `month_avg_quality` VALUES (45, '2018', '09', 404.48);
INSERT INTO `month_avg_quality` VALUES (46, '2018', '10', 403.46);
INSERT INTO `month_avg_quality` VALUES (47, '2018', '11', 410.14);
INSERT INTO `month_avg_quality` VALUES (48, '2018', '12', 392.68);
INSERT INTO `month_avg_quality` VALUES (49, '2019', '01', 387.06);
INSERT INTO `month_avg_quality` VALUES (50, '2019', '02', 396.74);
INSERT INTO `month_avg_quality` VALUES (51, '2019', '03', 405.14);
INSERT INTO `month_avg_quality` VALUES (52, '2019', '04', 408.68);
INSERT INTO `month_avg_quality` VALUES (53, '2019', '05', 358.63);
INSERT INTO `month_avg_quality` VALUES (54, '2019', '06', 346.83);
INSERT INTO `month_avg_quality` VALUES (55, '2019', '07', 351.54);
INSERT INTO `month_avg_quality` VALUES (56, '2019', '08', 347.87);
INSERT INTO `month_avg_quality` VALUES (57, '2019', '09', 351.79);
INSERT INTO `month_avg_quality` VALUES (58, '2019', '10', 348.51);
INSERT INTO `month_avg_quality` VALUES (59, '2019', '11', 354.92);
INSERT INTO `month_avg_quality` VALUES (60, '2019', '12', 348.4);

SET FOREIGN_KEY_CHECKS = 1;
