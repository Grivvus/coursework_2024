-- check that new order deliver date > than old one

CREATE OR REPLACE FUNCTION check_new_date_is_older() RETURNS TRIGGER
LANGUAGE plpgsql
as $$
DECLARE old_date timestamp with time zone;
BEGIN
	old_date := "deliver_date" from public."order" where (NEW."id" = "id");
	if old_date >= new."deliver_date" then
		RAISE EXCEPTION 'Error';
	end if;
	RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_control_prod_cnt
BEFORE UPDATE ON public."order" FOR EACH ROW
EXECUTE PROCEDURE check_new_date_is_older();
