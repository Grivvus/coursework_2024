-- вывести товар + покупатель, который покупал его чаще всего
select  "pid" product_id, "user_id"
from (
(
	select "user_id", "product_id", count(*) cnt
	from public."order_product" inner join public."order"
	on "order_id" = "id"
	group by "user_id", "product_id")
	inner join (
		select "product_id" pid, max(cnt) mcnt
		from (select "user_id", "product_id", count(*) cnt
		from public."order_product" inner join public."order"
		on "order_id" = "id"
		group by "user_id", "product_id")
		group  by "product_id"
	) subt
	on "product_id" = "pid" and "cnt" = "mcnt")
order by "pid"
