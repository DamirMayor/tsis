create table phonebook2 (
    name varchar(100) not null,
    phone text not null
);

insert into phonebook2(name,phone)
values('Bob','+77475009988');
insert into phonebook2(name,phone)
values('Alice','+77018884433');

select * from phonebook2;

-- 2

create or replace procedure addpls(
   addname varchar(100), 
   addphone text 
)
language plpgsql    
as $$
begin
    if exists (select 1 from phonebook2 where phonebook2.name = addname) then
		  update phonebook2 
		  set phone = addpls.addphone
		  where name = addpls.addname;
	  else
	 	  insert into phonebook2 values
		  (addname, addphone);
    end if;    
    commit;
end;$$;

call addpls('Bob', '+77475554455')
call addpls('Ansar', '+77477019865')

-- 3

create or replace procedure addmany(
    in names varchar[],
    in phones varchar[]
)
language plpgsql
as $$
declare
    i int;
    total_users int;
    result record;
begin
    if array_length(names, 1) != array_length(phones, 1) then
        raise exception 'Number of names and phones must be the same';
    end if;

    total_users := array_length(names, 1);

    for i in 1..total_users loop
        -- Check if phone number is in correct format
        if length(phones[i]) != 12 or phones[i] !~ '^(\+7700|\+7701|\+7702|\+7705|\+7706|\+7707|\+7708|\+7747|\+7771|\+7775|\+7776|\+7777|\+7778)\d{7}$' then
            -- Return incorrect data
            raise notice 'Incorrect phone format for user: % - %', names[i], phones[i];
		elsif length(phones[i]) = 12 and phones[i] !~ '^(\+7700|\+7701|\+7702|\+7705|\+7706|\+7707|\+7708|\+7747|\+7771|\+7775|\+7776|\+7777|\+7778)\d{7}$' then
			-- Insert user into the phonebook table
			insert into phonebook2 (name, phone) values (names[i], phones[i]);
        else
            -- Insert user into the phonebook table
            insert into phonebook2 (name, phone) values (names[i], phones[i]);
        end if;
    end loop;
    commit;

    raise notice 'Data has been inserted successfully';
end;$$;


do $$
declare
    names varchar[] := array['Erlan', 'Meruert', 'Alina', 'Erasyl', 'Damir'];
    phones varchar[] := array['+77011234567', '+70011234567', '+77051234567', '+77031234567', '+77771234567']; -- First phone number is correct, others are incorrect
begin
    -- Call the addmany procedure
    call addmany(names, phones);
end;$$;

select * from phonebook2;

-- 5

create or replace procedure delbyphone(
	todeluser varchar(100)
)
language plpgsql
as $$
begin
	if exists (select 1 from phonebook2 where phonebook2.phone = todeluser) then
		delete from phonebook2
		where phone = todeluser;
	end if;
	commit;
end;$$;

create or replace procedure delbyname(
	todeluser1 varchar(100)
)
language plpgsql
as $$
begin
	if exists (select 1 from phonebook2 where phonebook2.name = todeluser1) then
		delete from phonebook2
		where name = todeluser1;
	end if;
	commit;
end;$$;

select * from phonebook2

call delbyname('Bob')
call delbyphone('+77477019865')

-- drop table or procedure by using

drop procedure addmany
drop procedure delbyphone
drop procedure delbyname
drop procedure addpls
drop table phonebook2
