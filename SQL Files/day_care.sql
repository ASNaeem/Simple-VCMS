Create table day_care (day_care_id int auto_increment  primary key,
                animal_id int,
		dos date,
                start_time time,
                end_time time,
                notes TEXT
);

insert into day_care (animal_id, dos, start_time, end_time, notes) values (1, '2020-01-25', "09:30", "17:00", 'allergic to dairy');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (8, '2022-12-28', "15:00" , "20:00", 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (9, '2021-08-12', "12:00", "14:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (4, '2021-01-05', "13:00", "17:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (9, '2020-10-31', "10:00", "13:00", 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (6, '2022-05-28', "11:00", "20:00", 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (6, '2020-06-10', "12:00", "14:00", 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (3, '2020-03-08', "13:00", "17:00", 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (1, '2022-03-02', "15:00" , "20:00", 'allergic to beef');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (3, '2020-12-26', "12:00", "14:00", 'allergic to egg');
