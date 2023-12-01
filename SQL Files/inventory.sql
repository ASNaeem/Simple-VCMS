Create table inventory (item_id int auto_increment primary key,
		name varchar(45),
                mng_id int,            
                manufacturer varchar(50),
                item_type varchar(50),
                price decimal(10,2),
                amount int
                );
insert into inventory (name, mng_id, manufacturer, item_type, price, amount) values (1,"Carprofen","Rimadyl","Tablet",1606.47,61);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (2,"Clavamox","Clavulanic Acid","Tablet",970.05,9);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (3,"Baytril","Enrofloxacin","Tablet",1474.47,77);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (4,"Metacam","Meloxicam","Injection",2290.18,7);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (5,"Convenia","Cefovecin","Ointment",2924.3,9);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (6,"Heartgard","Nitenpyram","Cream",2747.87,7);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (7,"Panacur","Johnson & Johnson","Topical Cream",1632.83,7);
insert into inventory (mng_id, name, manufacturer, item_type, price, amount) values (8,"Revolution","Burt's Bees","lotion",2912.56,17);
