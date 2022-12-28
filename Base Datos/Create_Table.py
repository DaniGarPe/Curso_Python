import mysql.connector

conexionBBDD = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="2018UPA@",
	database="XXXXXXXXXX____XXXXXXXXXXXX")

print(conexionBBDD)
cursor = conexionBBDD.cursor()
cursor.execute("CREATE TABLE clientes ( \
	id INT AUTO_INCREMENT PRIMARY KEY, \
	nombre VARCHAR(255), \
	apellidos VARCHAR(255), \
	idProvincia INT)")

cursor.execute("CREATE TABLE provincias ( \
	id INT AUTO_INCREMENT PRIMARY KEY, \
	provincia VARCHAR(255))")

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")