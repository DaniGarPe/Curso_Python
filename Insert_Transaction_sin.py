import mysql.connector

# https://pynative.com/python-mysql-transaction-management-using-commit-rollback/
# from mysql.connector import Error
# from mysql.connector import errorcode
try:
	conexionBBDD = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="2018UPA@",
		database="XXXXXXXXXX____XXXXXXXXXXXX"
	)
	cursor = conexionBBDD.cursor()
	
	# conexionBBDD.autocommit = False  # will NOT put MySQL back into autocommit mode
	# (con esto controlamos todas en bloque SI pero si alguna falla 'pa tras')
	conexionBBDD.autocommit = True  # will put MySQL back into autocommit mode
	# (las consultas que funcionen "se las traga" y las que no pues NO)
	print ("Modo autocommit " + str(conexionBBDD.autocommit))
	consulta_sql = "INSERT INTO provincias (provincia) VALUES (%s)"
	valores =[
		("Madrid",),
		("Barcelona",),
		("Alicante",),
		("Tarragona",),
		("Sevilla",)
	] 
	cursor.executemany(consulta_sql, valores)

	consulta_sql = "INSERT INTO clientes (nombre, apellidos, idProvincia) VALUES (%s, %s, %s)"
	valores = ("María", "Gutierrez López", 1)
	cursor.execute(consulta_sql, valores)
	# print(cursor.rowcount, "record inserted.")

	consulta_sql = "INSERT INTO clientes (nombre, apellidos, idProvincia) VALUES (%s, %s, %s)" 
	# Prevent SQL Injection
	# It is considered a good practice to escape the values of any query
	# This is to prevent SQL injections, which is a common web hacking technique
	# to destroy or misuse your database.
	# The mysql.connector module uses the placeholder %s to escape values
	valores = ("Pedro", "López Román", 2)
	cursor.execute(consulta_sql, valores)
	# print(cursor.rowcount, "record inserted.")

	
except mysql.connector.Error as error:
	print("Failed to update record to database rollback: {}".format(error))

	if error.errno == mysql.connector.errorcode.ER_NO_SUCH_TABLE:
		# https://www.briandunning.com/error-codes/?source=MySQL
		print("\nTabla no existe")
	if error.errno == mysql.connector.errorcode.ER_BAD_FIELD_ERROR:
		# https://www.briandunning.com/error-codes/?source=MySQL
		print("\nCampo no existe")
	if error.errno == mysql.connector.errorcode.ER_WRONG_VALUE_COUNT_ON_ROW:
		print("\nEl número de valores no coincide con el número de campos en la consulta")		
finally:
	# closing database connection.
	if(conexionBBDD.is_connected()):
		cursor.close()
		conexionBBDD.close()
		print("connection is closed")


input("Press ENTER to EXIT")