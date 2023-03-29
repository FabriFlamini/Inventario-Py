import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "a1234",
     #port = "3306",
    database = "invetario"
)
#print(conn)


cursor = conn.cursor()

#sql = """CREATE TABLE Productos(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR (255), precio INT(255), cantidad INT(255))"""
#sql = """CREATE TABLE Clientes(nombre VARCHAR(255), direccion VARCHAR(255))"""
sql = """INSERT INTO Clientes (nombre, direccion) VALUES (%s, %s)"""
valores = {
    ("Miguel Zamora", "Buenos Aires"),
}
#cursor.execute(sql, valores)
cursor.executemany(sql, valores)

conn.commit()

print(cursor.rowcount, "registro insertado")

#cursor.execute("SHOW TABLES")

#cursor.execute("CREATE DATEBASE inventario")
#cursor.execute("SHOW DATABASES")
#for bd in cursor:
#   print(bd)



conn.close()
