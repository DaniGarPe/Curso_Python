import mysql.connector

conexionBBDD = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="2018UPA@",
		database="XXXXXXXXXX____XXXXXXXXXXXX"
	)
conexionBBDD.autocommit = True
cursor = conexionBBDD.cursor()
sql = "UPDATE clientes SET apellidos =%s WHERE nombre =%s"
valores = ("Lópezzzzzzzzzzzzzzzzzzz", "Pedro")
cursor.execute(sql, valores)
# conexionBBDD.commit()
print(cursor.rowcount, "record(s) affected")

#Retrieving data
sql = "SELECT * from clientes"

#Executing the query
cursor.execute(sql)

#Displaying the result
print(cursor.fetchall())

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")