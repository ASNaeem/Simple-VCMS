create table employees (
	id int auto_increment primary key,
	name varchar(45), email varchar(100),
	password varchar(50), address varchar(100),
	designation varchar(10), access_level int,
	working_hours varchar(50), salary decimal(10,2),
	joining_date date);
create table phone(
	     id int, phone varchar(16) primary key);
create table appointment(
             id int auto_increment primary key,
             animal_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100));
create table expenses (expense_id int auto auto_increment primary key,
		issuer_id int,
                handler_id int,               
                expense_date date;
                handle_date date,
                amount decimal(10,2),
                justification varchar(100));
Create table item(item_id int auto_increment primary key,
		name varchar(45),
                mng_id int            
                manufacturer varchar(50),
                item_type varchar(50),
                price decimal(10,2),
                amount int
                );

