create trigger generate_bill
after insert on appointments
for each row
begin
    declare service_cost decimal(10, 2);
    declare total_cost decimal(10, 2);
    declare hourly_cost decimal(10, 2);

    select cost into service_cost from services where service_id = new.service_id;

    if new.daycare_hours is not null and new.daycare_hours > 0 then
        -- inserting data to daycare table
        insert into daycare (apt_id, service_date)
        values (new.apt_id, new.apt_date);
        -- calculating total cost if daycare service was taken
        set total_cost = (200 * new.daycare_hours) + service_cost;
    else
        -- calculating total cost without daycare service
        set total_cost = service_cost;
    end if;

    -- generating the billing for appointment
    insert into billings (apt_id, bill_date, total_cost, status)
    values (new.apt_id, now(), total_cost, 'pending');
end;
$$
delimiter ;