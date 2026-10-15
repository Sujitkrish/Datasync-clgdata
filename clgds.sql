create database collage_info
create table  std_info(
	Student_ID varchar(10),	
	First_Name varchar(10),
	Last_Name varchar(10),	
	Major varchar(10),	
	std_Year varchar(5),	
	GPA decimal
);

create table course_reg(
	CourseID varchar(10),	
	CourseName varchar(10),	
	Professor varchar(10),	
	Credits int,	
	Semester varchar(10),	
	Status varchar(10)

);
select * from std_info
select * from course_reg