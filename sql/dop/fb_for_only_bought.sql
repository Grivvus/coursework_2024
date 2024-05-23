-- триггер должен допускать отзыв пользователя только на купленные товары
CREATE OR REPLACE FUNCTION feedback_is_correct() RETURNS TRIGGER
LANGUAGE plpgsql
as $$
BEGIN
    if NEW."user_id" not in 
(
select "user_id" from public."order" 
where "id" in (
	select "order_id" from public."order_product"
	where "product_id" = NEW."product_id"
)) then
    RAISE EXCEPTION 'Error';
    end if;
	RETURN NEW;
END;
$$;

CREATE TRIGGER check_feedback_is_correct 
BEFORE INSERT ON public."order" FOR EACH ROW
EXECUTE PROCEDURE feedback_is_correct();

-- test
insert into public."feedback" ("user_id", "product_id", "text", "rate")
values (1, 2, 'оч хороший товар, хотя не покупал, хз', 5);
