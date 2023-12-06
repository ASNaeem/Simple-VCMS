-- SQLBook: Code
create table employees (id int auto_increment primary key, name varchar(45), email varchar(100), password varchar(50), address varchar(100), designation varchar(10), access_level int, working_hours varchar(50), salary decimal(10,2), joining_date date);

insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Marie-jeanne MacGinney', 'mmacginney0@goo.gl', 'pE9"''*''E', '49517 Mayfield Parkway', 'Manager', 2, '7am - 3pm', 32568.01, '2022-09-23');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Korey MacCaull', 'kmaccaull1@multiply.com', 'lU6{)3gfw', '25 Hoard Terrace', 'Manager', 3, '7am - 3pm', 45196.66, '2022-06-04');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Avivah Barnard', 'abarnard2@mayoclinic.com', 'lF7*b!yxT#Vy8s', '766 Schmedeman Terrace', 'Manager', 3, '11pm - 7am', 27244.32, '2022-05-08');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Fred Nelsen', 'fnelsen3@ed.gov', 'zI9>ZBaM}{NWN', '44 Becker Court', 'Manager', 2, '3pm - 11pm', 18299.92, '2022-11-20');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Lola Rossetti', 'lrossetti4@howstuffworks.com', 'xB1}}S?Z', '32 Tony Alley', 'General Staff', 3, '7am - 3pm', 32075.0, '2022-07-13');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Maryl Skacel', 'mskacel5@alibaba.com', 'sS1!+ZWYl_l''s"n', '8 Pleasure Plaza', 'Receptionist', 3, '3pm - 11pm', 14217.02, '2022-11-19');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Ethelbert Huckstepp', 'ehuckstepp6@myspace.com', 'kT9~ONq{(L4', '22385 Duke Terrace', 'Veterinarian', 2, '7am - 3pm', 14082.95, '2022-06-22');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Shayne Laydel', 'slaydel7@tinypic.com', 'yG7-~@<>cAoPYD68', '46453 Lukken Road', 'Manager', 1, '9am - 5pm', 35247.04, '2022-04-23');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Ayn Masseo', 'amasseo8@discuz.net', 'gG1&ia|_<', '738 Becker Court', 'Veterinarian', 3, '3pm - 11pm', 20005.48, '2022-09-05');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) values ('Emlynn Leipoldt', 'eleipoldt9@flavors.me', 'uW6?9y3qG''''&6', '8202 Michigan Alley', 'Manager', 1, '9am - 5pm', 23582.69, '2022-04-19');

CREATE TRIGGER after_delete_employee
After delete
on employees 
for each row
Begin
Delete from phone id=OLD.id;
End;
