/*
 Navicat Premium Data Transfer

 Source Server         : 本机服务
 Source Server Type    : MySQL
 Source Server Version : 50634
 Source Host           : localhost
 Source Database       : spider

 Target Server Type    : MySQL
 Target Server Version : 50634
 File Encoding         : utf-8

 Date: 12/07/2016 02:26:15 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `doubandushu`
-- ----------------------------
DROP TABLE IF EXISTS `doubandushu`;
CREATE TABLE `doubandushu` (
  `id` varchar(40) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(40) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `imgurl` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
