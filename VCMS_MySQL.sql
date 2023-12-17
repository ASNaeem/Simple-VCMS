drop database VCMS;
create database if not exists VCMS;
use VCMS;
/* animal */
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

insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Ruby', '2020-03-16', 'no', 'male', 'Rabbit', 'Dutch Rabbit', 'Brown', 'Gets aggresive if someone tries to hold for a long period of time. Might bite.', 
		'Valera Schleicher', 'vschleicher0@upenn.edu', '+7-555-802-2801', '549 Center Hill', '2022-03-14', 'injured');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Sky', '2020-04-10', 'no', 'Female', 'Bird', 'Parrot', 'Green', 'Pecks.', 
		'Niven Synan', 'nsynan1@earthlink.net', '+352-586-400-3477', '728 Rusk Circle', '2023-08-10', 'healthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Clay', '2022-05-28', 'no', 'male', 'Cat', 'Local Breed', 'Jet Black', 'Good Boy.', 
		'Tamanna K', 'tamannak@gmail.com', '01827453830', 'Rajabari, Genda, Savar', '2023-11-25', 'injured');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Oreo', '2018-12-30', 'no', 'female', 'cat', 'Persian', 'Brown, White, Black Mixed', 'None.', 
		'Jesse Adamolli', 'jadamolli3@vk.com', '+86-216-370-8399', '2531 Bultman Court', '2023-10-07', 'healthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Nugget', '2022-01-02', 'no', 'female', 'chicken', 'Silkie', 'Brown-Black', 'None', 
		'Gracie Wyper', 'gwyper4@simplemachines.org', '+351-321-443-3930', '3011 Bellgrove Court', '2022-08-23', 'unhealthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Fox','2022-11-23','yes','female','dog','husky','white','none',
         'Alvis','awitheridge0@about.com','+789-553-4487','1 Blaine Trail','2023-11-28','unhealthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Colobus','2022-12-3','yes','male','Dog','Husky','White','none',
        'Idalia','iroutledge1@chicagotribune.com','+886-582-2049','0 Logan Park','2023-10-30','healthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('chic','2023-12-2','no','male','Chicken','Pakistani','black','none',
        'Ahona','bmcgilroy9@biblegateway.com','+783-157-2333','8 Anderson Circle','2023-08-13','unhealthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Lava gull','2022-11-10','no','female','bird','Dove','Black and white','none',
        'Ahona','fdelisle6@abc.net.au','+820-407-9734','631 Blaine Road','2023-07-08','healthy');
insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Luci','2022-10-3','no','female','Cat','Persian','brown','none',
        'Amalee','acruwys8@google.co.uk','+551-882-1092','2719 Springview Junction','2023-07-14','injured');
 /* employee */
create table employees (employee_id int auto_increment primary key, name varchar(45), email varchar(100), password varchar(50), address varchar(100), designation varchar(50), access_level int, working_hours varchar(50), salary decimal(10,2), joining_date date, employee_status varchar(10));

insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('VCMS Admin', 'admin@vcms.com', 'admin', 'vet clinic', 'Admin', 4, '7:00 - 15:00', 50000, '2023-01-01', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Marie-jeanne MacGinney', 'mmacginney0@goo.gl', 'pE9"''*''E', '49517 Mayfield Parkway', 'Manager', 2, '7:00 - 15:00', 32568.01, '2022-09-23', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Korey MacCaull', 'kmaccaull1@multiply.com', 'lU6{)3gfw', '25 Hoard Terrace', 'Manager', 3, '7:00 - 15:00', 45196.66, '2022-06-04', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Avivah Barnard', 'abarnard2@mayoclinic.com', 'lF7*b!yxT#Vy8s', '766 Schmedeman Terrace', 'Manager', 3, '11:00 - 10:00', 27244.32, '2022-05-08', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Fred Nelsen', 'fnelsen3@ed.gov', 'zI9>ZBaM}{NWN', '44 Becker Court', 'Manager', 2, '9:00 - 21:00', 18299.92, '2022-11-20', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Lola Rossetti', 'lrossetti4@howstuffworks.com', 'xB1}}S?Z', '32 Tony Alley', 'General Staff', 3, '7:00 - 15:00', 32075.0, '2022-07-13', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Maryl Skacel', 'mskacel5@alibaba.com', 'sS1!+ZWYl_l''s"n', '8 Pleasure Plaza', 'Receptionist', 3, '9:00 - 11:00', 14217.02, '2022-11-19', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Ethelbert Huckstepp', 'ehuckstepp6@myspace.com', 'kT9~ONq{(L4', '22385 Duke Terrace', 'Veterinarian', 2, '7:00 - 15:00', 14082.95, '2022-06-22', 'On leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Shayne Laydel', 'slaydel7@tinypic.com', 'yG7-~@<>cAoPYD68', '46453 Lukken Road', 'Manager', 1, '9:00 - 17:00', 35247.04, '2022-04-23', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Ayn Masseo', 'amasseo8@discuz.net', 'gG1&ia|_<', '738 Becker Court', 'Veterinarian', 3, '9:00 - 11:00', 20005.48, '2022-09-05', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Emlynn Leipoldt', 'eleipoldt9@flavors.me', 'uW6?9y3qG''''&6', '8202 Michigan Alley', 'Manager', 1, '9:00 - 17:00', 23582.69, '2022-04-19', 'Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Sibilla Boswood','sboswood0@unc.edu','$2a$04','0515 Harper Place','Manager',4,'10:35',15507,'2023-06-02','Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Desdemona Lillee','dlillee1@drupal.org','$2a$04$','2 Algoma Terrace','general employee',3,'7:00- 15:00',13981,'2023-07-18','on leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Carmencita Yoxall','cyoxall2@pagesperso-orange.fr','$2a$04$04cF','1 Sloan Crossing','recieptionsist',2,'8:00 -21:00',5417,'2023-08-15','on leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Alysa Broker','abroker3@hud.gov','$2a$04$q','33 Holmberg Junction','Veterinarian',1,'9:00 - 22:00',12448,'2023-04-26','Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Gertrud Netherwood','gnetherwood4@bloglines.com','.66NwXoYqieE','476 Birchwood Point','Manager',4,'9:00 - 22:00',19730,'2023-05-10','on leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Sisely Ramsay','sramsay5@sohu.com','rgZmk5pG2OsXd','77176 Badeau Trail','general employee',3,'9:00 - 17:00',858,'2023-04-18','on leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Mellie Crunkhurn','mcrunkhurn6@pen.io','HSCa9k8An0e6Mc','3 Bay Hill','recieptionsist',2,'9:00 - 22:00',29503,'2023-07-06','on leave');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Athena Mitskevich','amitskevich7@seesaa.net', '2a$04','3073 Macpherson Alley','Veterinarian',1,'10:00- 20:00',20237,'2023-07-11','Working');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date, employee_status) values ('Ollie Flye','oflye8@twitpic.com','2ahjj','1647 Bowman Alley','Manager',4, '9:00 -22:00',16433,'2023-10-21','Working');

 /* services */
Create table services( service_id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2), 
                service_details text,
                service_availability varchar(10));

insert into services (name, cost, service_details, service_availability) values ('Regular Checkup', 500, 'Routine examination to monitor and maintain pet health.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Flu Vaccine', 1500, 'Prevents influenza in pets through vaccination.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Wound Dressing', 300, 'Care for injuries through proper wound cleaning and dressing.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Spay', 1500, 'Surgical procedure to sterilize and prevent reproduction in females.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('C-Section', 5000, 'Surgical delivery for complications during pet childbirth.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Rabies Vaccine', 500, 'Essential protection against deadly rabies virus for animals.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Neuter', 1000, 'Surgical procedure to sterilize and prevent reproduction in males animals', 'Yes');

      
/* appointment*/
create table appointments (
             appointment_id int auto_increment primary key,
             animal_id int,
			 employee_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100),
             constraint fk_animal_id_app foreign key (animal_id) references animals (animal_id) on delete cascade,
			  constraint fk_employee_id_app foreign key (employee_id) references employees (employee_id) on delete cascade

);
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,9, '2022-01-21', '15:00', 'Neuter', 'scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (2,18, '2021-05-30', '10:00', 'Regular Checkup', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (3,9, '2022-12-11', '15:00', 'Rabies Vaccine', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (4,14, '2020-04-11', '12:00', 'C-Section', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (5,18, '2020-10-12', '11:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,7, '2021-07-26', '14:00', 'Wound Dressing', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (7,7, '2020-12-10', '10:00', 'Spay', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (8,14, '2020-04-28', '15:00', 'Flu Vaccine', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (9,7, '2021-04-30', '15:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,7, '2023-09-23', '11:23',' c- section', 'scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (2,9,'2023-02-28','14:45','neuter','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (3,18,'2023-10-10','16:56','dental care','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,7, '2023-06-17','15:52' , 'c- section',' completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (5,18, '2023-03-26','18:26','vaccination','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,14,'2023-09-27','19:12','vaccination','cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,7,'2023-09-27','19:12','vaccination','cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (8,7,'2023-02-23','16:29','c- section','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (9,9,'2023-05-08','10:05','c- section','completed');

/* day_care*/
Create table day_care (day_care_id int auto_increment  primary key,
                animal_id int,
		dos date,
                start_time time,
                end_time time,
                notes TEXT,
                constraint fk_animal_id_day foreign key (animal_id) references animals (animal_id) on delete cascade
);

insert into day_care (animal_id, dos, start_time, end_time, notes) values (1, '2020-01-25', "09:30", "17:00", 'allergic to dairy');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (2, '2022-12-28', "15:00" , "20:00", 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (3, '2021-08-12', "12:00", "14:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (4, '2021-01-05', "13:00", "17:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (5, '2020-10-31', "10:00", "13:00", 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (6, '2022-05-28', "11:00", "20:00", 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (7, '2020-06-10', "12:00", "14:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (8, '2020-03-08', "13:00", "17:00", 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (9, '2022-03-02', "15:00" , "20:00", 'allergic to beef');

/* bill*/
create table billings (
	bid int auto_increment primary key,
	day_care_id int,
	aid int,
	billing_date date,
	total_amount DECIMAL(8,2),
	adjustment DECIMAL(8,2),
	status varchar(10) DEFAULT "Due",
     constraint fk_appointment_id foreign key(aid) references appointments (appointment_id) on delete cascade);

insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (1, 4, "2022-01-21", 1500.00, 300.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (null, 2, "2021-05-30", 1000.00, 550.00, "Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (3, 3, "2022-12-11", 1800.00, 280.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (4, 4, "2020-04-11", 1500.00, 650.00,"Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (5, 6, "2020-10-12", 1000.00, 100.00,"Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (1, 1, "2022-01-21", 1500.00, 300.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (2, 7, "2021-05-30", 1000.00, 550.00, "Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (null, 3, "2022-12-11", 1800.00, 280.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (4, 8, "2020-04-11", 1500.00, 650.00,"Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (null, 5, "2020-10-12", 1000.00, 100.00,"Paid");

/* expenses */
Create table expenses (expense_id int  auto_increment primary key,
		issuer_id int, 
		handler_id int,              
                expense_date date,
				handle_date date,
                amount decimal(10,2),
                justification varchar(100),
                constraint fk_issuer_id foreign key (issuer_id) references employees (employee_id)on delete cascade);
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 10,1, '2022-01-24','2022-01-25', 9453.71, 'New lights was bought for the clinic');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 9,2, '2022-12-23','2022-12-24' ,9456.01, 'An order for a rare medicine was placed with an advanced payment.');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 8,3, '2023-02-27','2023-02-07', 7579.5, 'reason for the expense was to repair the x-ray machine');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 7,4,'2023-03-16','2023-03-17', 4426.23, 'Surgery equipment was changed');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 6,5,'2023-04-26','2023-04-27', 4651.62, 'Air conditioner servicing was done this was the cost');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 5,6,'2023-05-23','2023-05-25', 2052.58, 'Toiletries was bought');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 4,7,'2023-05-29','2023-06-30', 9274.36, 'reason for the expense was to repair the x-ray machine');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date, amount, justification) values ( 3,8,'2023-06-23','2023-06-23', 2016.62, 'updated the emergency medicine stock so this was the cost');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 2,9, '2023-07-13','2023-07-13', 2820.38, 'Toiletries was bought');
insert into expenses ( issuer_id,handler_id, expense_date, handle_date,  amount, justification) values ( 1,10,'2023-07-23','2023-07-24', 9700.27, 'New lights was bought for the clinic');

/* phones */
create table phones (employee_id int, phone varchar(50) primary key, 
             constraint fk_employee_id_phones foreign key(employee_id) references employees (employee_id) on delete cascade);

insert into phones (employee_id, phone)values (1, '+880-155-240-7452');
insert into phones (employee_id, phone)values (1, '+880-155-545-8888');
insert into phones (employee_id, phone)values (2, '+880-155-550-7452');
insert into phones (employee_id, phone)values (2, '+880-155-555-8888');
insert into phones (employee_id, phone)values (3, '+880-115-553-3834');
insert into phones (employee_id, phone)values (3, '+880-195-550-0422');
insert into phones (employee_id, phone)values (4, '+880-115-552-7181');
insert into phones (employee_id, phone)values (4, '+880-115-559-7397');
insert into phones (employee_id, phone)values (5, '+880-185-558-5645');
insert into phones (employee_id, phone)values (5, '+880-185-554-2563');
insert into phones (employee_id, phone)values (6, '+880-115-553-3505');
insert into phones (employee_id, phone)values (6, '+880-185-559-1210');
insert into phones (employee_id, phone)values (7, '+880-155-551-2280');
insert into phones (employee_id, phone)values (7, '+880-175-558-9049');
insert into phones (employee_id, phone)values (8, '+880-185-554-1326');
insert into phones (employee_id, phone)values (8, '+880-185-556-9427');
insert into phones (employee_id, phone)values (9, '+880-115-553-3523');
insert into phones (employee_id, phone)values (9, '+880-165-552-4421');
insert into phones (employee_id, phone)values (10, '+880-115-558-9381');
insert into phones (employee_id, phone)values (10, '+880-175-559-8778');
insert into phones (employee_id, phone)values (11, '+880-155-240-7454');
insert into phones (employee_id, phone)values (11, '+880-155-545-8898');
insert into phones (employee_id, phone)values (12, '+880-155-550-7472');
insert into phones (employee_id, phone)values (12, '+880-155-555-7888');
insert into phones (employee_id, phone)values (13, '+880-115-553-2834');
insert into phones (employee_id, phone)values (13, '+880-195-550-1422');
insert into phones (employee_id, phone)values (14, '+880-115-552-7182');
insert into phones (employee_id, phone)values (14, '+880-115-559-7387');
insert into phones (employee_id, phone)values (15, '+880-185-558-5745');
insert into phones (employee_id, phone)values (15, '+880-185-554-2553');
insert into phones (employee_id, phone)values (16, '+880-115-553-3555');
insert into phones (employee_id, phone)values (16, '+880-185-559-1310');
insert into phones (employee_id, phone)values (17, '+880-155-551-2180');
insert into phones (employee_id, phone)values (17, '+880-175-558-1049');

/* record */
create table record (
	animal_id INT,
	record TEXT,
	rdate DATE,
    constraint fk_animal_id_rec foreign key (animal_id) references animals (animal_id)
    on delete cascade
);
insert into record (animal_id, record, rdate) values (1, 'Got bit by a cat in the leg.', '2023-01-31');
insert into record (animal_id, record, rdate) values (3, 'Got into fight with another cat, got bitten by a cat on front leg.', '2023-09-13');
insert into record (animal_id, record, rdate) values (3, 'Twisted left back leg, having trouble walking.', '2022-12-08');
insert into record (animal_id, record, rdate) values (4, 'Had a fight.', '2023-10-15');
insert into record (animal_id, record, rdate) values (5, 'Feathers are falling of off the skin for some unknown  reason.', '2023-10-18');
insert into record (animal_id, record, rdate) values (6, 'experienced lethargy and decreased appetite for two days.', '2022-03-10');
insert into record (animal_id, record, rdate) values (7, 'a history of vomiting and diarrhea for the past 24 hours', '2022-02-03');
insert into record (animal_id, record, rdate) values (8, 'a history of excessive urination and water consumption for the past 2 weeks.', '2023-08-24');
insert into record (animal_id, record, rdate) values (9, 'a history of seizures for the past 6 months.', '2023-06-09');
insert into record (animal_id, record, rdate) values (8, 'a history of chronic urinary tract infections for the past 3 years.', '2022-12-23');
insert into record (animal_id, record, rdate) values (7, 'Got bit by a cat in the leg.', '2023-01-31');
insert into record (animal_id, record, rdate) values (3, 'Got into fight with another cat, got bitten by a cat on front leg.', '2023-09-13');
insert into record (animal_id, record, rdate) values (3, 'Twisted left back leg, having trouble walking.', '2022-12-08');
insert into record (animal_id, record, rdate) values (4, 'Had a fight.', '2023-10-15');
insert into record (animal_id, record, rdate) values (5, 'Feathers are falling of off the skin for some unknown  reason.', '2023-10-18');
insert into record (animal_id, record, rdate) values (6, 'experienced lethargy and decreased appetite for two days.', '2022-03-10');
insert into record (animal_id, record, rdate) values (7, 'a history of vomiting and diarrhea for the past 24 hours', '2022-02-03');
insert into record (animal_id, record, rdate) values (8, 'a history of excessive urination and water consumption for the past 2 weeks.', '2023-08-24');
insert into record (animal_id, record, rdate) values (9, 'a history of seizures for the past 6 months.', '2023-06-09');
insert into record (animal_id, record, rdate) values (1, 'a history of chronic urinary tract infections for the past 3 years.', '2022-12-23');


/*billing_services*/

create table bill_services (
	bid int,
	service_id int,
    constraint fk_bid_bill foreign key (bid) references billings (bid) on delete cascade,
    constraint fk_service_id foreign key (service_id) references services (service_id) on delete cascade
);

insert into bill_services (bid, service_id) values (1,1);
insert into bill_services(bid, service_id) values(1,2);
insert into bill_services (bid, service_id) values (2,2);
insert into bill_services(bid, service_id) values(2,4);
insert into bill_services (bid, service_id) values (3,3);
insert into bill_services(bid, service_id) values(3,2);
insert into bill_services (bid, service_id) values (4,1);
insert into bill_services(bid, service_id) values(4,2);
insert into bill_services (bid, service_id) values (6,4);
insert into bill_services(bid, service_id) values(6,2);
insert into bill_services (bid, service_id) values (7,2);
insert into bill_services(bid, service_id) values(2,5);
insert into bill_services (bid, service_id) values (3,7);
insert into bill_services(bid, service_id) values(5,2);
insert into bill_services (bid, service_id) values (8,4);
insert into bill_services(bid, service_id) values(9,2);

alter table employees drop column working_hours;

DELIMITER //

CREATE PROCEDURE CreateBillingForAppointment(
    IN p_appointment_id INT,
    IN p_day_care_id INT
)
BEGIN
    -- Insert into billings table with initial values
    INSERT INTO billings (day_care_id, aid, billing_date, total_amount, adjustment, status)
    VALUES (p_day_care_id, p_appointment_id, CURDATE(), 0.00, 0.00, 'Scheduled');
END;

//
DELIMITER ;

create user if not exists 'vcms-admin'@'localhost' identified by 'admin';
grant all privileges on vcms.* to 'vcms-admin'@'localhost';
flush privileges;