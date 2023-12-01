-- SQLBook: Code
create table animals (
	animals_id int auto_increment primary key,
	animals_name varchar(50),
	birth_date date,
	sterilized varchar(5);
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

insert into animals (animals_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Ruby', '2020-03-16', 'yes', 'male', 'Rabbit', 'Dutch Rabbit', 'Brown', 'Gets aggresive if someone tries to hold for a long period of time. Might bite.', 
		'Valera Schleicher', 'vschleicher0@upenn.edu', '+7-555-802-2801', '549 Center Hill', '2022-03-14', 'injured');
insert into animals (animals_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Sky', '2020-04-10', 'no', 'Female', 'Bird', 'Parrot', 'Green', 'Pecks.', 
		'Niven Synan', 'nsynan1@earthlink.net', '+352-586-400-3477', '728 Rusk Circle', '2023-08-10', 'healthy');
insert into animals (animals_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Clay', '2022-05-28', 'no', 'male', 'Cat', 'Local Breed', 'Jet Black', 'Good Boy.', 
		'Tamanna K', 'tamannak@gmail.com', '01827453830', 'Rajabari, Genda, Savar', '2023-11-25', 'injured');
insert into animals (animals_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Oreo', '2018-12-30', 'no', 'female', 'cat', 'Persian', 'Brown, White, Black Mixed', 'None.', 
		'Jesse Adamolli', 'jadamolli3@vk.com', '+86-216-370-8399', '2531 Bultman Court', '2023-10-07', 'healthy');
insert into animals (animals_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
					owner_name, email, phone, address, reg_date, med_condition) 
values ('Nugget', '2022-01-02', 'no', 'female', 'chicken', 'Silkie', 'Brown-Black', 'None', 
		'Gracie Wyper', 'gwyper4@simplemachines.org', '+351-321-443-3930', '3011 Bellgrove Court', '2022-08-23', 'unhealthy');