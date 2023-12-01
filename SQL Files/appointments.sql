create table appointments (
             id int auto_increment primary key,
             animal_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100)
);
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (4, '2022-01-21', '15:00', 'Neuter', 'scheduled');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (4, '2021-05-30', '10:00', 'Regular Checkup', 'completed');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (9, '2022-12-11', '15:00', 'Rabies Vaccine', 'cancelled');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (6, '2020-04-11', '12:00', 'C-Section', 'cancelled');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (7, '2020-10-12', '11:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (8, '2021-07-26', '14:00', 'Wound Dressing', 'completed');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (3, '2020-12-10', '10:00', 'Spay', 'cancelled');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (10, '2020-04-28', '15:00', 'Flu Vaccine', 'cancelled');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (7, '2021-04-30', '15:00', 'Rabies Vaccine', 'completed');
insert into appointments (animal_id, a_date, a_time, visit_reason, a_status) values (8, '2022-05-25', '14:00', 'Regular Checkup', 'completed');
