-- SQLBook: Code
create table animal(id int primary key auto_increment, 
                    name varchar(50), 
                    reg_date date, 
                    species varchar(20),  
                    breed varchar(30),
                    color varchar(20), 
                    gender varchar(10),
                    birth_date date,
                    sterilized varchar(5),
                    current_condition  varchar(100),
                    behave_warning varchar(100),
                    oname varchar(50),
                    email varchar(100),
                    phone varchar(20),
                    address varchar(100));

create table records(id int, record varchar(100), rdate date);

create table bill()


#create table phone(id int, phone varchar(16) primary key)

#alter table employees rename column employee_id to id;



Create table service( id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2),
                details varchar(50), 
                availability boolean);

Create table day_care( dos date,
                start_time time,
                end_time time,
                s_hours int,
                penalty_per_hour decimal(10,2),
                status varchar(50),
                id int);
Create table item( id int auto_increment primary key, 
                name varchar(45),
                manufacture varchar(50),
                i_type varchar(50),
                amount int,
                price decimal(10,2), 
                id int);

create table appointment(id int auto_increment primary key, a_time time a_date date, visit_reason varchar(100), a_status varchar(100));
create table veterinarian(id int auto_increment primary key, spec varchar(100), totalcase int);