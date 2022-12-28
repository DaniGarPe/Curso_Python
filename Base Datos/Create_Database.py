import mysql.connector

# establishing the connection
conexionBBDD = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="2018UPA@"
	)

print(conexionBBDD)

# you must create a Cursor object. It will let
# you execute all the queries you need

cursor = conexionBBDD.cursor()
NombreBaseDatos = "XXXXXXXXXX____XXXXXXXXXXXX"
cursor.execute("CREATE DATABASE " + NombreBaseDatos)

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")