-- function that counts summary cost of all items in order by order id

CREATE OR REPLACE FUNCTION count_order_cost(in ord_id int)
    RETURNS numeric
AS $$
DECLARE 
    _res numeric;
BEGIN
    select sum("price"*"cnt") into _res
    from public."order_product" inner join public."product"
    on "id" = "product_id"
    where "order_id" = ord_id
    group by "order_id";
END
$$ LANGUAGE plpgsql;
