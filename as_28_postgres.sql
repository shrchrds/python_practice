create DATABASE ass;
use ass;

/*1. Create a table (student) with 3 columns (rollno, name, course). */

create table student (roll_no int, student_name text, course text);


/* 2. Insert records for 4 students. */

insert into student values (100, 'Ashok', 'Python'),
                            (101, 'Harsh', 'Data Science'),
                            (102, 'Mak', 'Java'),
                            (103, 'Sahil', 'Job guarantee C');

/* 3. Write a Select query to fetch all the students. */

SELECT * from student;

/* 4. Update the student name of rollno 3 with ‘Mohan’ */

update student set student_name = 'Mohan' where roll_no = 103;

/* 5. Delete any student from table with their rollno. */

delete from student where roll_no = 103;

/* 6. Delete all the data from student table. */
delete from student;

/* 7. Drop the student table. */
drop table student;

/* 8. Create Courses table (cid, cname) where cid is a primary key and Student table
(rollno, name, cid) where rollno is a primary key and cid is a foreign key.*/

create table courses (course_id int, course_name text, PRIMARY KEY  (course_id));


create table Student (roll_no int, student_name text, course_id int, PRIMARY KEY (roll_no), 
                    constraint fk_cid Foreign Key (course_id) REFERENCES courses(course_id));

/* 9. Insert data in both the tables. */

insert into courses values (1, 'Python'), (2, 'Big Data'), (3, 'Java'), (4, 'Data Science');


insert into Student values (101, 'Ashok', 1), (102, 'Harsh', 2), (103, 'Mak', 3), (104, 'Sahil', 4);


/* 10. Select all the students who are doing a specific course, eg. Python */

select * from Student where course_id = (select course_id from courses where course_name='Python' );