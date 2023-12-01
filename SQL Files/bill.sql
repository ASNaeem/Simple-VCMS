create table billings (
	bid int auto_increment primary key,
	day_care_id int
	aid int,
	payment_date date,
	total_amount DECIMAL(8,2),
	status varchar(10) DEFAULT "Due"
);

insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) values (1,1,1,"");
insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) values (2, 2, 1000.00);
insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) values (3, 3, 1800.00);
insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) values (4, 4, 1500.00);
insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) values (5, 5, 1000.00);
