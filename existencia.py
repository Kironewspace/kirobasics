import pyodbc


conn_str = pyodbc.connect(
 "DRIVER={SQL Server};SERVER=DESKTOP-5488JNB\MIGUEL;DATABASE=products;Trusted_Connection=yes;")

def agregar_existencias():

   id_producto = int(input("Ingrese el ID del producto: "))
   cantidad = int(input("Ingrese la cantidad de existencias a agregar: "))

   conn = conn_str
   cursor = conn.cursor()


   cursor.execute("SELECT existencias FROM products WHERE id_product = ?", id_producto)
   existencia_actual = cursor.fetchone()[0]

   nueva_existencia = existencia_actual + cantidad


   cursor.execute("UPDATE products SET existencias = ? WHERE id_product = ?", nueva_existencia, id_producto)
 
   

   conn.commit()
   conn.close()


print("cantidad agregada de manera satisfactoria")