Create table services( service_id int auto_increment primary key, 
                name varchar(45),
                cost decimal(10,2), 
                service_details varchar(50),
                service_availability varchar(10));

insert into services (name, cost, service_details, service_availability) values ('Regular Checkup', 500, 'Routine examination to monitor and maintain pet health.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Flu Vaccine', 1500, 'Prevents influenza in pets through vaccination.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Wound Dressing', 300, 'Care for injuries through proper wound cleaning and dressing.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Spay', 1500, 'Surgical procedure to sterilize and prevent reproduction in females.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('C-Section', 5000, 'Surgical delivery for complications during pet childbirth.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Rabies Vaccine', 500, 'Essential protection against deadly rabies virus for animals.', 'Yes');
insert into services (name, cost, service_details, service_availability) values ('Neuter', 1000, 'Surgical procedure to sterilize and prevent reproduction in males animals', 'Yes');