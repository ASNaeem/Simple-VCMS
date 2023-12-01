Create table expenses (expense_id int auto auto_increment primary key,
		issuer_id int,
                handler_id int,               
                expense_date date;
                handle_date date,
                amount decimal(10,2),
                justification varchar(100));
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (6, '2022-01-24', '2022-01-23', 9453.71, 'New lights was bought for the clinic');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (1, '2022-12-23', '2022-12-22', 9456.01, 'An order for a rare medicine was placed with an advanced payment.');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (6, '2023-02-27', '2023-02-26', 7579.5, 'reason for the expense was to repair the x-ray machine');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (6, '2023-03-16', '2023-03-15', 4426.23, 'Surgery equipment was changed');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (6, '2023-04-26', '2023-04-25', 4651.62, 'Air conditioner servicing was done this was the cost');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (9, '2023-05-23', '2023-05-22', 2052.58, 'Toiletries was bought');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (9, '2023-05-29', '2023-05-28', 9274.36, 'reason for the expense was to repair the x-ray machine');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (9, '2023-06-23', '2023-06-25', 2016.62, 'updated the emergency medicine stock so this was the cost');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (2, '2023-07-13', '2023-07-14', 2820.38, 'Toiletries was bought');
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values (2, '2023-07-23', '2023-07-24', 9700.27, 'New lights was bought for the clinic');
