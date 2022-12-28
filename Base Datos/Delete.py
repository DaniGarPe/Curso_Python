import mysql.connector

conexionBBDD = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="2018UPA@",
		database="XXXXXXXXXX____XXXXXXXXXXXX"
	)
conexionBBDD.autocommit = True
cursor = conexionBBDD.cursor()
sql = "DELETE FROM clientes"
cursor.execute(sql)
# conexionBBDD.commit()
print(cursor.rowcount, "record(s) deleted")

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")