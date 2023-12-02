create database if not exists VCMS;
use VCMS;
drop table if exists employees;
drop table if exists phones;
drop table if exists animals;
drop table if exists appointments;
drop table if exists expenses;
drop table if exists inventory;
drop table if exists services;
drop table if exists veterinarians;
drop table if exists records;
drop table if exists day_care;
drop table if exists billings;
drop table if exists bill_services;
create table employees (
	employee_id int auto_increment primary key,
	name varchar(45), email varchar(100),
	password varchar(50), address varchar(100),
	designation varchar(10), access_level int,
	working_hours varchar(50), salary decimal(10,2),
	joining_date date
);
create table phones (
	     employee_id int, phone varchar(50) primary key
);
create table animals (
	animal_id int auto_increment primary key,
	animal_name varchar(50),
	birth_date date,
	sterilized varchar(5),
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
create table appointments (
             appointment_id int auto_increment primary key,
             animal_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100)
);
create table expenses (expense_id int auto_increment primary key,
		issuer_id int,
                handler_id int,               
                expense_date date,
                handle_date date,
                amount decimal(10,2),
                justification varchar(100)
);
Create table inventory (item_id int auto_increment primary key,
		name varchar(45),
                mng_id int,            
                manufacturer varchar(50),
                item_type varchar(50),
                price decimal(10,2),
                amount int
);
Create table services (service_id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2),
		service_details varchar(50),
                service_availability varchar(5) 
                
);
create table veterinarians (
             employee_id int,
             totalcase int,
             specialization varchar(100)
);
create table records (record_id int auto_increment primary key, 
	animal_id INT,
	record TEXT,
	rdate DATE
);
Create table day_care (day_care_id int auto_increment  primary key,
                animal_id int,
		dos date,
                start_time time,
                end_time time,
                notes TEXT
);
create table billings (
	bid int,
	day_care_id int,
	aid int,
	payment_date date,
	total_amount DECIMAL(8,2),
	status varchar(10)
);
create table bill_services (
	bid int,
	service_id int
);