-- check that rate of feedback in range [1, 5]

CREATE OR REPLACE FUNCTION check_rate() RETURNS TRIGGER
LANGUAGE plpgsql
as $$
BEGIN
	if NEW."rate" > 5 or NEW."rate" < 1 then
		RAISE EXCEPTION 'Error';
	end if;
	RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_reate
BEFORE INSERT ON public."feedback" FOR EACH ROW
EXECUTE PROCEDURE check_rate();

CREATE TRIGGER trigger_check_reate
BEFORE UPDATE ON public."feedback" FOR EACH ROW
EXECUTE PROCEDURE check_rate();

-- test 
insert into public."feedback" ("user_id", "text", "rate", "product_id")
values (3, 'test text 123', -1, 1);
insert into public."feedback" ("user_id", "text", "rate", "product_id")
values (3, 'test text 123', 6, 1);

