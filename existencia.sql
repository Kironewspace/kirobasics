create database products

use products

create table products(
id_product int primary key,
codigo_producto nvarchar (14) not null,
nombre_producto nvarchar (30) not null,
existencias int not null,
precio int not null


);






INSERT INTO products (id_product, codigo_producto, nombre_producto, existencias, precio)
VALUES
(1, 123456789012, 'Camiseta azul', 10, 20),
(2, 987654321098, 'Zapatos deportivos', 5, 50),
(3, 012345678901, 'Libro de cocina', 2, 35),
(4, 123456789013, 'Televisor LED', 10, 1000),
(5, 987654321099, 'Celular de última generación', 5, 5000),
(6, 012345678902, 'Computadora portátil', 2, 20000),
(7, 123456789014, 'Bicicleta de montaña', 10, 500),
(8, 987654321010, 'Equipo de sonido', 5, 10000),
(9, 012345678903, 'Juegos de video', 2, 200);

select * from products

CREATE TRIGGER eliminar_producto_agotado
ON products
FOR UPDATE
AS
BEGIN
    DECLARE @id_producto int;
    SET @id_producto = (SELECT id_product FROM inserted);

    IF (SELECT existencias FROM products WHERE id_product = @id_producto) = 0
    BEGIN  -- Se agregó el bloque BEGIN
        DELETE FROM products WHERE id_product = @id_producto;
    END  -- Se agregó el bloque END
END;
