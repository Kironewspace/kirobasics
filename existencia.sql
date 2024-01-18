create database products

use products

create table products(
id_product int primary key,
codigo_producto nvarchar (14) not null,
nombre_producto nvarchar (30) not null,
existencias int not null,
precio int not null


);
