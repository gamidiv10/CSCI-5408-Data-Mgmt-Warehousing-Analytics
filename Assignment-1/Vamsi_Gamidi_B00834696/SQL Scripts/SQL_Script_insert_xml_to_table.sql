mysql -h localhost -u root -p --local-infile


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\advisers.xml' INTO TABLE adviser ROWS IDENTIFIED BY '<Adviser>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\archives.xml' INTO TABLE archive ROWS IDENTIFIED BY '<Archive>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\climbing_programs.xml' INTO TABLE climbing_programs ROWS IDENTIFIED BY '<Climbing_Program>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\dalplex_camps.xml' INTO TABLE dalplex_camps ROWS IDENTIFIED BY '<Dalplex_Camp>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\faculty.xml' INTO TABLE faculty ROWS IDENTIFIED BY '<faculty>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\grad_courses.xml' INTO TABLE grad_courses ROWS IDENTIFIED BY '<Course>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\grad_programs.xml' INTO TABLE grad_programs ROWS IDENTIFIED BY '<Grad_Program>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\group_fitness_classes.xml' INTO TABLE group_fitness_classes ROWS IDENTIFIED BY '<Fitness_Class>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\libraries.xml' INTO TABLE libraries ROWS IDENTIFIED BY '<Library_Name>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\payment_methods.xml' INTO TABLE payment_methods ROWS IDENTIFIED BY '<Payment_Method>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\research_clusters.xml' INTO TABLE research_clusters ROWS IDENTIFIED BY '<Research_Cluster>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\residences.xml' INTO TABLE residences ROWS IDENTIFIED BY '<Residence>';


LOAD XML LOCAL INFILE 'C:\\Users\\vamsi\\Desktop\\Python\\undergrad_programs.xml' INTO TABLE undergrad_programs ROWS IDENTIFIED BY '<Undergrad_Program>';


