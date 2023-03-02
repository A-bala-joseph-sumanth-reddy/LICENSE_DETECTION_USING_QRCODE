qrcodercdata/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - qrcode
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`qrcode` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `qrcode`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`password`) values ('admin','admin');

/*Table structure for table `rcdata` */

DROP TABLE IF EXISTS `rcdata`;

CREATE TABLE `rcdata` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `regno` varchar(100) DEFAULT NULL,
  `regowner` varchar(100) DEFAULT NULL,
  `address` varchar(500) DEFAULT NULL,
  `mclass` varchar(100) DEFAULT NULL,
  `vclass` varchar(100) DEFAULT NULL,
  `mfgyr` varchar(100) DEFAULT NULL,
  `fuelused` varchar(100) DEFAULT NULL,
  `bodytype` varchar(100) DEFAULT NULL,
  `cnumber` varchar(100) DEFAULT NULL,
  `enumber` varchar(100) DEFAULT NULL,
  `cc` varchar(100) DEFAULT NULL,
  `wbase` varchar(100) DEFAULT NULL,
  `scapacity` varchar(100) DEFAULT NULL,
  `uweight` varchar(100) DEFAULT NULL,
  `colour` varchar(100) DEFAULT NULL,
  `regdate` varchar(100) DEFAULT NULL,
  `validity` varchar(100) DEFAULT NULL,
  `tax` varchar(100) DEFAULT NULL,
  `hto` varchar(100) DEFAULT NULL,
  `osign` varchar(10000) DEFAULT NULL,
  `asign` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rcdata` */

insert  into `rcdata`(`id`,`regno`,`regowner`,`address`,`mclass`,`vclass`,`mfgyr`,`fuelused`,`bodytype`,`cnumber`,`enumber`,`cc`,`wbase`,`scapacity`,`uweight`,`colour`,`regdate`,`validity`,`tax`,`hto`,`osign`,`asign`) values (1,'123','qwe','asd','asdf','CHEVITIKALLU','2020-04-17','asdad','sdfsdf','12','dfgdfg','CHEVITIKALLU','sdfs','CHEVITIKALLU','24','green','10/04/2020','07/04/2035','231','tvs','nav-logo.jpg','nav-logo.jpg');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(19) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`,`dob`,`email`,`address`,`mobile`) values (13,'bhushan','123','2020-04-21','nani.nagabhushanam@gmail.com','moula ali','0123456789');

/*Table structure for table `userdata` */

DROP TABLE IF EXISTS `userdata`;

CREATE TABLE `userdata` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `hno` varchar(100) DEFAULT NULL,
  `colony` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `mandal` varchar(100) DEFAULT NULL,
  `dist` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `issue` varchar(100) DEFAULT NULL,
  `validity` varchar(100) DEFAULT NULL,
  `rta` varchar(100) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `usersign` varchar(100) DEFAULT NULL,
  `authoritysign` varchar(100) DEFAULT NULL,
  `ref` varchar(100) DEFAULT NULL,
  `vtype` varchar(100) DEFAULT NULL,
  `badge` varchar(100) DEFAULT NULL,
  `bloodgroup` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `userdata` */

insert  into `userdata`(`id`,`name`,`fname`,`dob`,`hno`,`colony`,`location`,`mandal`,`dist`,`pin`,`issue`,`validity`,`rta`,`photo`,`usersign`,`authoritysign`,`ref`,`vtype`,`badge`,`bloodgroup`) values (4,'nagabhushanam','nageswararao','2020-04-21','NEAR RCM CHURCH','3-119','521180','uppal','medcahl','521180','07/04/2020','07/04/2023','uppal','ne.png','ne.png','Emblem_of_India.png','123','two wheeler','123','0+'),(5,'nagabhushanam','nageswararao','2020-04-18','NEAR RCM CHURCH','3-119','521180','uppal','medcahl','521180','10/04/2020','10/04/2023','uppal','Emblem_of_India.png','logo.jpg','nav-logo.jpg','123','two wheeler','123','0+');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
