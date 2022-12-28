import mysql.connector

conexionBBDD = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="2018UPA@",
	database="XXXXXXXXXX____XXXXXXXXXXXX"
)
cursor = conexionBBDD.cursor()

conexionBBDD.autocommit = True  # will put MySQL back into autocommit mode

consulta_sql = "INSERT INTO provincias (provincia) VALUES (%s)"
valores = ("Provincia XXXXXXXXXXXXXXXXXXXXXXXX",)

cursor.execute(consulta_sql, valores)

idProvincia = cursor.lastrowid  # recuperamos el id (autonumérico) de la consulta anterior


print("1 record inserted, ID:", idProvincia)

consulta_sql = "INSERT INTO clientes (nombre, apellidos, idProvincia) VALUES (%s, %s, %s)"
valores = [
    ('Peter', 'Lowstreet 4', idProvincia),
    ('Amy', 'Apple st 652', idProvincia),
    ('Hannah', 'Mountain 21', idProvincia),
    ('Michael', 'Valley 345', idProvincia),
    ('Sandy', 'Ocean blvd 2', idProvincia),
    ('Betty', 'Green Grass 1', idProvincia),
    ('Richard', 'Sky st 331', idProvincia),
    ('Susan', 'One way 98', idProvincia),
    ('Vicky', 'Yellow Garden 2', idProvincia),
    ('Ben', 'Park Lane 38', idProvincia),
    ('William', 'Central st 954', idProvincia),
    ('Chuck', 'Main Road 989', idProvincia),
    ('Viola', 'Sideway 1633', idProvincia)
]

cursor.executemany(consulta_sql, valores)

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")