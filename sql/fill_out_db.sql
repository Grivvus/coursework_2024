insert into public."admin" ("passport_series", "passport_number", "living_address", "place_of_residence", "first_name", "second_name", "email", "phone_number", "password")
values ('0000', '123456', 'г. Москва ул. Пушкина д. 22', 'г. Москва ул. Пушкина д. 22', 'Админ', 'Админов', 'admin@admail.com', '83336662020', '1bbd886460827015e5d605ed44252251');
-- hash from "11111111"

insert into public."manufacturer" ("name")
values ('MSI');
insert into public."manufacturer" ("name")
values ('asus');
insert into public."manufacturer" ("name")
values ('Samsung');
insert into public."manufacturer" ("name")
values ('Apple');
insert into public."manufacturer" ("name")
values ('Xiaomi');
insert into public."manufacturer" ("name")
values ('Gigabyte');
insert into public."manufacturer" ("name")
values ('Ardor Gaming');

insert into public."product_type" ("name")
values('Комплектующие ПК');
insert into public."product_type" ("name")
values('Ноутбуки');
insert into public."product_type" ("name")
values('Смартфоны');
insert into public."product_type" ("name")
values('Планшеты');
insert into public."product_type" ("name")
values('Компьютерная периферия');
insert into public."product_type" ("name")
values('Носимая электроника');
insert into public."product_type" ("name")
values('Фотоаппараты');

insert into public."picup_point" ("physical_address")
values ('г. Саратов, Ново-Астраханское ш. зд. 107');
insert into public."picup_point" ("physical_address")
values ('г. Саратов, ул. Политехническая, дом 75, корпус 2');
insert into public."picup_point" ("physical_address")
values ('г. Саратов, им Ордженикидзе Г.К., дом 1');

insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('Aorus gaming x570 wifi', 1.00, 5, 'test description, change in future', '/path/to/photo', 1, 2);
insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('MSI PRO MP251 24', 1.00, 5, 'test description, change in future', '/path/to/photo', 5, 7);
insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('Samsung Odyssey G5 C27G55TQWI', 1.00, 5, 'test description, change in future', '/path/to/photo', 5, 5);
insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('Xiaomi 13 256G', 1.00, 5, 'test description, change in future', '/path/to/photo', 3, 3);
insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('Apple IPhone 14 256G', 1.00, 5, 'test description, change in future', '/path/to/photo', 3, 4);
insert into public."product" ("name", "price", "in_stock", "description", "photo", "product_type_id", "manufacturer_id")
values ('Xiaomi band 8', 1.00, 5, 'test description, change in future', '/path/to/photo', 6, 3);

insert into public."order" ("date", "deliver_date", "picup_point_id", "user_id")
values ('2021-03-15', '2021-03-18', 1, 3);
insert into public."order" ("date", "deliver_date", "picup_point_id", "user_id")
values ('2023-07-21', '2023-07-22', 2, 2);
insert into public."order" ("date", "deliver_date", "picup_point_id", "user_id")
values ('2020-02-01', '2020-02-07', 1, 5);
insert into public."order" ("date", "deliver_date", "picup_point_id", "user_id")
values ('2023-03-03', '2023-03-06', 3, 1);

insert into public."order_product" ("order_id", "product_id", "cnt")
values (1, 1, 1);
insert into public."order_product" ("order_id", "product_id", "cnt")
values (1, 2, 2);
insert into public."order_product" ("order_id", "product_id", "cnt")
values (2, 3, 1);
insert into public."order_product" ("order_id", "product_id", "cnt")
values (3, 4, 1);
insert into public."order_product" ("order_id", "product_id", "cnt")
values (3, 6, 1);
insert into public."order_product" ("order_id", "product_id", "cnt")
values (4, 1, 2);

