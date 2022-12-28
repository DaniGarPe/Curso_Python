import mysql.connector

conexionBBDD = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="2018UPA@",
	database="XXXXXXXXXX____XXXXXXXXXXXX"
)

cursor = conexionBBDD.cursor()

sql = "SELECT \
		C.nombre AS Nombre, \
		C.apellidos AS Apellidos, \
		P.provincia AS Provincia \
	FROM \
		clientes AS C INNER JOIN provincias AS P \
	ON C.idprovincia = P.id"


print(sql + "\n")

cursor.execute(sql)

myresult = cursor.fetchall()

for x in myresult:
	print(x)

# Closing the connection
cursor.close()
conexionBBDD.close()
input("Press ENTER to EXIT")