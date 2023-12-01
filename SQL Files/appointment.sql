create table appointment(
             id int auto_increment primary key,
             animal_id int,
             a_date date,
             a_time time,
             visit_reason varchar(100),
             a_status varchar(100));

insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (13, '2023/03/15', '10:26 AM', 'Flu Vaccine', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (12, '2023/08/12', '2:21 PM', 'Rabies Vaccine', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (17, '2023/06/09', '8:02 PM', 'Spay', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (1, '2023/03/07', '1:12 PM', 'Flu Vaccine', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (16, '2023/11/23', '12:51 PM', 'Neuter', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (5, '2023/06/29', '4:59 PM', 'Neuter', 'cancelled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (14, '2023/07/09', '11:20 AM', 'Flu Vaccine', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (9, '2023/04/29', '3:15 PM', 'Spay', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (6, '2023/06/14', '1:28 PM', 'Neuter', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (7, '2023/07/16', '6:10 PM', 'Regular Checkup', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (12, '2023/03/21', '3:48 PM', 'C-Section', 'cancelled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (18, '2022/12/29', '8:55 PM', 'Regular Checkup', 'cancelled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (12, '2023/01/28', '6:41 PM', 'Flu Vaccine', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (6, '2023/09/22', '12:36 PM', 'C-Section', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (12, '2022/12/04', '2:22 PM', 'C-Section', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (18, '2023/01/07', '1:58 PM', 'Regular Checkup', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (20, '2023/01/20', '8:38 PM', 'C-Section', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (17, '2023/09/07', '5:45 PM', 'Wound Dressing', 'completed');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (9, '2023/06/19', '10:55 AM', 'Wound Dressing', 'scheduled');
insert into appointment (id, animal_id, a_date, a_time, visit_reason, a_status) values (1, '2023/06/12', '11:03 AM', 'Neuter', 'scheduled');
