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
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,1, '2022-01-21', '15:00', 'Neuter', 'scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (2,2, '2021-05-30', '10:00', 'Regular Checkup', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (3,3, '2022-12-11', '15:00', 'Rabies Vaccine', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (4,4, '2020-04-11', '12:00', 'C-Section', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (5,5, '2020-10-12', '11:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,6, '2021-07-26', '14:00', 'Wound Dressing', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (7,7, '2020-12-10', '10:00', 'Spay', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (8,8, '2020-04-28', '15:00', 'Flu Vaccine', 'cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (9,9, '2021-04-30', '15:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (10,10, '2022-05-25', '14:00', 'Regular Checkup', 'completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,1, '2023-09-23', '11:23',' c- section', 'scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (2,2,'2023-02-28','14:45','neuter','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (3,3,'2023-10-10','16:56','dental care','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (1,4, '2023-06-17',' 15:52' , 'c- section',' completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (5,5, '2023-03-26',' 18:26','vaccination','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,6,'2023-09-27','19:12','vaccination','cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (6,7,'2023-09-27','19:12','vaccination','cancelled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (8,8,'2023-02-23','16:29','c- section','scheduled');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (9,9,'2023-05-08','10:05','c- section','completed');
insert into appointments (animal_id, employee_id, a_date, a_time, visit_reason, a_status) values (10,10, '2023-05-25', '14:00', 'Regular Checkup', 'completed');
