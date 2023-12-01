drop database VCMS;
create database VCMS;
use VCMS;
drop table if exists employees;
create table employees (
	id int auto_increment primary key,
	name varchar(45), email varchar(100),
	password varchar(50), address varchar(100),
	designation varchar(10), access_level int,
	working_hours varchar(50), salary decimal(10,2),
	joining_date date
);
drop table if exists phones;
create table phones (
	     id int, phone varchar(16) primary key
);
drop table if exists animals;
create table animals (
	animal_id int auto_increment primary key,
	animal_name varchar(50),
	birth_date date,
	sterilized bool,
	gender varchar(10),
	species varchar(50),
	breed varchar(50),
	color varchar(50),
	behavioral_warning TEXT,
	owner_name varchar(50),
	email varchar(50),
	phone varchar(20),
	address varchar(50),
	reg_date date,
	med_condition TEXT
);
drop table if exists appointments;
create table appointments (
             id int auto_increment primary key,
             animal_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100)
);
drop table if exists expenses;
create table expenses (expense_id int auto auto_increment primary key,
		issuer_id int,
                handler_id int,               
                expense_date date;
                handle_date date,
                amount decimal(10,2),
                justification varchar(100)
);
drop table if exists inventorys;
Create table inventorys (item_id int auto_increment primary key,
		name varchar(45),
                mng_id int            
                manufacturer varchar(50),
                item_type varchar(50),
                price decimal(10,2),
                amount int
);
drop table if exists services;
Create table services ( id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2),
                availability boolean, 
                details varchar(50)
);
drop table if exists veterinarians;
create table veterinarians (
             id int,
             totalcase int,
             specialization varchar(100)
);
drop table if exists records;
create table records (
	id INT,
	record TEXT,
	rdate DATE
);
drop table if exists day_care;
Create table day_care (animal_id int,
		dos date,
                start_time time,
                end_time time,
                notes TEXT
);
drop table if exists billings;
create table billings (
	bid int,
	day_care_id int
	aid int,
	payment_date date,
	total_amount DECIMAL(8,2),
	status varchar(10)
);
drop table if exists bill_services;
create table bill_services (
	bid int,
	service_id int
);