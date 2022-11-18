#Este archivo convierte un csv en una base de datos
import pandas as pd
import sqlite3 as sq3

#Establecer conexión, si no hay se crea la base de datos
con = sq3.connect("preciosJumbo.db")
#Crear objeto cursor
cur = con.cursor()

#Query para crear la tabla almacenado en una variable string
crear_tabla = '''CREATE TABLE tablaPreciosJumbo 
(indice,nombres,precios);
'''
#Ejecución del query para crear la tabla
cur.execute(crear_tabla)

#Leer el archivo con Pandas
datos = pd.read_csv('preciosJumbo.csv')
#Insertar los datos a la tabla que nombraremos covid
datos.to_sql('tablaPreciosJumbo', con, if_exists='append', index=False)

#Guardar cambios en la base de datos
con.commit()
#Cerrar conexión con la base de datos
con.close()