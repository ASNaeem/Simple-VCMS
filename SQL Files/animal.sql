-- SQLBook: Code
create table animals (
	animal_id INT auto_increment primary key,
	animal_name varchar(50),
	birth_date date,
);
animal_name:str, 
birth_date:str,
sterilized:bool, 
gender:str, 
species:str, 
breed:str, 
color:str, 
behavioral_warning:str, 
owner_name:str, 
email:str, 
phone:str, 
address:str, 
reg_date:str, 
med_condition:str = None

insert into animal (id, name, reg_date, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email, phone, address) values (1, 'Ruby', '2022-03-14', 'Rabbit', 'Dutch Rabbit', 'Brown', 'male', '2020-03-16', 'yes', 'injured', 'Gets aggresive if someone tries to hold for a long period of time. Might bite.', 'Valera Schleicher', 'vschleicher0@upenn.edu', '+7-555-802-2801', '549 Center Hill');
insert into animal (id, name, reg_date, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email, phone, address) values (2, 'Sky', '2023-08-10', 'Bird', 'Parrot', 'Green', 'female', '2020-04-10', 'no', 'healthy', 'Pecks.', 'Niven Synan', 'nsynan1@earthlink.net', '+352-586-400-3477', '728 Rusk Circle');
insert into animal (id, name, reg_date, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email, phone, address) values (3, 'Clay', '2023-11-25', 'Cat', 'Local Breed', 'Jet Black', 'male', '2022-05-28', 'no', 'injured', 'Good Boy.', 'Tamanna K', 'tamannak@gmail.com', '01827453830', 'Rajabari, Genda, Savar');
insert into animal (id, name, reg_date, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email, phone, address) values (4, 'Oreo', '2023-10-07', 'cat', 'Persian', 'Brown, White, Black Mixed', 'female', '2018-12-30', 'no', 'healthy', 'None.', 'Jesse Adamolli', 'jadamolli3@vk.com', '+86-216-370-8399', '2531 Bultman Court');
insert into animal (id, name, reg_date, species, breed, color, gender, birth_date, sterilized, current_condition, behavioral_warning, oname, email, phone, address) values (5, 'Nugget', '2022-08-23', 'chicken', 'Silkie', 'Brown-Black', 'female', '2022-01-02', 'no', 'unhealthy', 'None', 'Gracie Wyper', 'gwyper4@simplemachines.org', '+351-321-443-3930', '3011 Bellgrove Court');