insert into animals (animal_name, birth_date, sterilized, gender, species, breed, color, behavioral_warning, 
		owner_name, email, phone, address, reg_date, med_condition) 
values ('Ruby', '2020-03-16', 'yes', 'male', 'Rabbit', 'Dutch Rabbit', 'Brown', 'Gets aggresive if someone tries to hold for a long period of time. Might bite.', 
		'Valera Schleicher', 'vschleicher0@upenn.edu', '+7-555-802-2801', '549 Center Hill', '2022-03-14', 'injured');
insert into employees (name, email, password, address, designation, access_level, working_hours, salary, joining_date) 
values ('Marie-jeanne MacGinney', 'mmacginney0@goo.gl', 'pE9"''*''E', '49517 Mayfield Parkway', 'Manager', 2, '7am - 3pm', 32568.01, '2022/09/23');
insert into appointments (id, animal_id, a_date, a_time, visit_reason, a_status) 
values (13, '2023/03/15', '10:26 AM', 'Flu Vaccine', 'completed');
insert into phones (id, phone) values (1, '+880-115-557-8653');
insert into phones (id, phone) values (1, '+880-115-552-5559');
insert into veterinarians (id, totalcase, specialization) 
values (1, 6, 'Veterinary Dermatologist');
insert into day_care (dos, start_time, end_time, notes) values ("2023-05-16", "7:42 PM","9:51 PM", "allergic to nut")
insert into billings (bid, day_care_id, aid, payment_date, total_amount, status) 
values (1, 1, 1, "2023-04-01" 2000.00);
insert into expenses (handler_id, expense_date, handle_date, amount, justification) 
values ( 1, '2022-12-23', '2023-02-26', 40195, 'reason for the expense was to repair the x-ray machine');
insert into inventory (name, mng_id, manufacturer, item_type, price, amount) 
values (1,"Carprofen","Rimadyl","Tablet",1606.47,61);
insert into records (id, record, rdate) values (1, 'Got bit by a cat in the leg.', '2023-01-31');

insert into bill_services(bid, service_id) values(1, 1);