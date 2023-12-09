create table billings (
	bid int auto_increment primary key,
	day_care_id int,
	aid int,
	billing_date date,
	total_amount DECIMAL(8,2),
	adjustment DECIMAL(8,2),
	status varchar(10) DEFAULT "Due"
);
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (1, 1, "", 1500.00, 300.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (2, 2, "", 1000.00, 550.00, "Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (3, 3, "", 1800.00, 280.00, "Due");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (4, 4, "", 1500.00, 650.00,"Paid");
insert into billings ( day_care_id, aid, billing_date, total_amount, adjustment, status) values (5, 5, "", 1000.00, 100.00,"Paid");

