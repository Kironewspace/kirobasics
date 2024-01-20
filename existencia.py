import pyodbc

# Configuración de la conexión a la base de datos
conn_str = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-5488JNB\MIGUEL;DATABASE=products;Trusted_Connection=yes;')

def agregar_existencias():
    id_producto = int(input("Ingrese el ID del producto: "))
    cantidad = int(input("Ingrese la cantidad de existencias a agregar: "))

    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Obtener la existencia actual del producto
    cursor.execute("SELECT existencias FROM productos WHERE id_producto = ?", id_producto)
    existencia_actual = cursor.fetchone()[0]

    # Calcular la nueva cantidad de existencia
    nueva_existencia = existencia_actual + cantidad

    # Actualizar la existencia en la tabla productos
    cursor.execute("UPDATE productos SET existencias = ? WHERE id_producto = ?", nueva_existencia, id_producto)
    conn.commit()

    conn.close()

if cursor.rowcount == 0:
 print("El producto con ID {} no existe.".format(id_producto))


