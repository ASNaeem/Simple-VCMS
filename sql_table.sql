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
                    owner_name varchar(50),
                    owner_email varchar(100),
                    owner_phone varchar(20),
                    owner_address varchar(100));

create table 


#create table phone(id int, phone varchar(16) primary key)

#alter table employees rename column employee_id to id;



Create table service( id int auto_increment primary key, 
Service name varchar(45),
Cost decimal(10,2),
Details varchar(50), 
Availability boolean);


create table appointment(id int auto_increment primary key, a_time time a_date date, visit_reason varchar(100), a_status varchar(100));
create table veterinarian(id int auto_increment primary key, spec varchar(100), totalcase int);