-- проверяет на каждое добавление товара в order_product,
-- что количество товара в заказе не превышает его количества на складе

CREATE OR REPLACE FUNCTION control_prod_cnt() RETURNS TRIGGER
LANGUAGE plpgsql
as $$
DECLARE cnt int;
BEGIN
	cnt := "in_stock" from public."product" where (NEW."product_id" = "id");
	if cnt < NEW."cnt" or NEW."cnt" < 0 then
		RAISE EXCEPTION 'Error';
	end if;
	RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_control_prod_cnt
BEFORE INSERT ON public."order_product" FOR EACH ROW
EXECUTE PROCEDURE control_prod_cnt();

-- test trigger
insert into public."order_product" ("order_id", "product_id", cnt)
values (1, 1, 18);
