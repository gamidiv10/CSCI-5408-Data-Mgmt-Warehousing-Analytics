CREATE TABLE `adviser` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(100) DEFAULT NULL,
  `Last_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `archive` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Archive_Submission` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `climbing_program` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Program` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `dalplex_camps` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Camp` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `faculty` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) DEFAULT NULL,
  `Office_No` varchar(100) DEFAULT NULL,
  `Faculty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `google_play_store` (
  `Application_Name` varchar(200) DEFAULT NULL,
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Rating` varchar(200) DEFAULT NULL,
  `Category` varchar(200) DEFAULT NULL,
  `Size` varchar(200) DEFAULT NULL,
  `Type` varchar(200) DEFAULT NULL,
  `Price` varchar(200) DEFAULT NULL,
  `Content_Rating` varchar(200) DEFAULT NULL,
  `Android_Version` varchar(200) DEFAULT NULL,
  `Current_Version` varchar(200) DEFAULT NULL,
  `Last_Update` varchar(200) DEFAULT NULL,
  `Number_Of_Installs` varchar(200) DEFAULT NULL,
  `Reviews` varchar(200) DEFAULT NULL,
  `Genres` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `googleplaystore_user_reviews` (
  `App` text,
  `Sentiment` text,
  `Sentiment_Polarity` double DEFAULT NULL,
  `Sentiment_Subjectivity` double DEFAULT NULL
);


CREATE TABLE `grad_courses` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Course` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `grad_programs` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Program` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `group_fitness_classes` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Class` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `libraries` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Library_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `payment_methods` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `payment` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `research_clusters` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Cluster` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `residences` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Residence_Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);


CREATE TABLE `undergrad_programs` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `program` varchar(100) DEFAULT NULL,
  `Faculty` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);
