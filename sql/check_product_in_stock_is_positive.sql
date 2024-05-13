-- проверяет на каждую вставку в product, что количество нового продукта неотрицательно
-- то же самое делает на обновление таблицы

CREATE OR REPLACE FUNCTION check_product_in_stock_ge0() RETURNS TRIGGER
LANGUAGE plpgsql
as $$
BEGIN
	if NEW."in_stock" < 0 then
		RAISE EXCEPTION 'Error';
	end if;
	RETURN NEW;
END;
$$;

CREATE TRIGGER check_on_insert_product_in_stock_ge0 -- >=0
BEFORE INSERT ON public."product" FOR EACH ROW
EXECUTE PROCEDURE check_product_in_stock_ge0();

CREATE TRIGGER check_on_update_product_in_stock_ge0
BEFORE UPDATE ON public."product" FOR EACH ROW
EXECUTE PROCEDURE check_product_in_stock_ge0();

-- test 
insert into public."product" ("price", "in_stock", "photo", "product_type_id", "manufacturer_id", "name", "description")
values (12.2, -1, '/test/path/to/photo', 1, 1, 'test_name', 'test description');
