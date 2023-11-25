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




#create table phone(id int, phone varchar(16) primary key)

#alter table employees rename column employee_id to id;



Create table service( id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2),
                Details varchar(50), 
                availability boolean);

Create table day_care(dos date, 
                start_time time, 
                end_time time, 
                s_hours int,
                pnalty_per_hour decimal(10,2), 
                status varchar(50),
                id int);

create table item(id int auto_increment primary key, 
                name varchar(50), 
                manufacture varchar(50), 
                i_type varchar(50), 
                price decimal(10,2), 
                amount int,
                id int);


