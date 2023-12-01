Create table expenses (expense_id int auto auto_increment primary key,
		issuer_id int,
                handler_id int,               
                expense_date date;
                handle_date date,
                amount decimal(10,2),
                justification varchar(100));
insert into expenses (handler_id, expense_date, handle_date, amount, justification) values ( 1, '2022-12-23', '2023-02-26', 40195, 'reason for the expense was to repair the x-ray machine');
insert into expenses (handler_id, handle_date, amount, justification) values ( 2, '2023-02-26', 45764, 'updated the emergency medicine stock so this was the cost');
insert into expenses (handler_id, handle_date, amount, justification) values ( 3, '2023-09-07', 19715, 'Air conditioner servicing was done this was the cost');
insert into expenses (handler_id, handle_date, amount, justification) values ( 4, '2023-08-19', 18399, 'new set of sofa was bought');
insert into expenses (handler_id, handle_date, amount, justification) values ( 5, '2023-04-09', 30975, 'New lights was bought for the clinic');
insert into expenses (handler_id, handle_date, amount, justification) values ( 6, '2023-06-10', 10270, 'Toiletries was bought');
insert into expenses (handler_id, handle_date, amount, justification) values ( 7, '2023-10-02', 34338, 'Surgery equipment was changed');
insert into expenses (handler_id, handle_date, amount, justification) values ( 8, '2023-07-27', 47462, 'An order for a rare medicine was placed with an advanced payment.');
insert into expenses (handler_id, handle_date, amount, justification) values ( 9, '2023-05-25', 9925, 'updated the emergency medicine stock so this was the cost');
insert into expenses (handler_id, handle_date, amount, justification) values ( 10, '2023-01-28', 15337, 'Air conditioner servicing was done this was the cost');
