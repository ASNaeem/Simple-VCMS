Create table inventory (item_id int auto_increment primary key,
		name varchar(45),           
                manufacturer varchar(50),
                item_type varchar(50),
                price decimal(10,2),
                amount int
                );
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Carprofen","Rimadyl","Tablet",1606.47,61);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Clavamox","Clavulanic Acid","Tablet",970.05,9);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Baytril","Enrofloxacin","Tablet",1474.47,77);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Metacam","Meloxicam","Injection",2290.18,7);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Convenia","Cefovecin","Ointment",2924.3,9);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Heartgard","Nitenpyram","Cream",2747.87,7);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Panacur","Johnson & Johnson","Topical Cream",1632.83,7);
insert into inventory ( name, manufacturer, item_type, price, amount) values ("Revolution","Burt's Bees","lotion",2912.56,17);
