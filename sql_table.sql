-- SQLBook: Code
create table animal (
	id INT,
	name VARCHAR(50),
	reg_date DATE,
	species VARCHAR(10),
	breed TEXT,
	color VARCHAR(50),
	gender VARCHAR(6),
	birth_date DATE,
	sterilized VARCHAR(3),
	current_condition VARCHAR(7),
	behavioral_warning TEXT,
	oname VARCHAR(50),
	email VARCHAR(50),
	phone VARCHAR(50),
	address VARCHAR(50)
);
create table record (
	id INT,
	record TEXT,
	rdate DATE
);
create table record (
	bid INT primary key auto_increment,
	aid INT,
	total_amount DECIMAL(10,2)
);

#create table phone(id int, phone varchar(16) primary key);

#alter table employees rename column employee_id to id;

Create table service( id int auto_increment primary key, 
<<<<<<< HEAD
                name varchar(45),
                cost decimal(10,2),
                details varchar(50), 
                availability boolean);
=======
                    name varchar(45),
                    cost decimal(10,2),
                    details varchar(50), 
                    availability boolean);
>>>>>>> d3253513d85154678cbc012abe64cd40e6629aed

Create table day_care(dos date,
                start_time time,
                end_time time,
                s_hours int,
                penalty_per_hour decimal(10,2),
                status varchar(50),
                app_id int);
Create table item( id int auto_increment primary key, 
                name varchar(45),
                manufacture varchar(50),
                i_type varchar(50),
                amount int,
                price decimal(10,2), 
                em_id int);

create table appointment(id int auto_increment primary key, animal_id int, a_date date, a_time time, visit_reason varchar(100), a_status varchar(100));
create table veterinarian(id int, spec varchar(100), totalcase int);