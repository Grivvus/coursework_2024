-- необходимо найти самого любимого производителя для пользователя
select "manufacturer_id"
from (select "manufacturer_id", count(manufacturer_id) as cnt
from (select * from (
select "user_id" uid, "id" oid from public."order"
where "user_id" = 1
) subt inner join public."order_product"
on "order_id" = "oid") subt2 inner join public."product"
on  "product_id" = public."product"."id"
group by manufacturer_id) 
where cnt = (select max(cnt) from (select count(*) as "cnt" from public."product" where "id" in 
(
    select distinct "product_id" from public."order_product" 
    where "product_id" in
(
        select "id" from public."order"
        where "user_id" = 1
))
group by "manufacturer_id"));
