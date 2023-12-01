Create table day_care (day_care_id int auto_increment  primary key,
                animal_id int,
		dos date,
                start_time time,
                end_time time,
                notes TEXT
);

insert into day_care (animal_id, dos, start_time, end_time, notes) values (1, '2020-01-25', 0.51, 14.68, 'allergic to dairy');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (8, '2022-12-28', 6.09, 5.63, 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (9, '2021-08-12', 5.33, 14.86, 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (4, '2021-01-05', 17.7, 17.49, 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (9, '2020-10-31', 12.59, 18.29, 'allergic to egg');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (6, '2022-05-28', 22.07, 6.11, 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (6, '2020-06-10', 15.96, 13.34, 'allergic to chicken');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (3, '2020-03-08', 0.24, 16.87, 'allergic to nut');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (1, '2022-03-02', 8.62, 16.64, 'allergic to beef');
insert into day_care (animal_id, dos, start_time, end_time, notes) values (3, '2020-12-26', 21.93, 20.84, 'allergic to egg');
