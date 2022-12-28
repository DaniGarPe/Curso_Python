import mysql.connector

conexionBBDD = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="2018UPA@",
	database="XXXXXXXXXX____XXXXXXXXXXXX"
)

cursor = conexionBBDD.cursor()
cursor.execute("SELECT id, nombre, apellidos FROM clientes")

# After executing the query, the MySQL server is ready to send the data.
# The result set could be zero rows, one row, or 100 million rows.
# Depending on the expected volume, you can use different techniques to process this result set.
# In this example, we use the cursor object as an iterator. 

for (id, nombre, apellidos) in cursor:
    print("{}, {} {}".format(id, nombre, apellidos))

print("\n\n")


cursor.execute("SELECT id, nombre, apellidos FROM clientes")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

print("\n\n")

cursor.execute("SELECT id, nombre, apellidos FROM clientes")
myresult = cursor.fetchall()
# We use the fetchall() method, which fetches all rows from the last executed statement.

# The fetchall() method retrieves all the rows in the result
# set of a query and returns them as list of tuples.

print(myresult)

print("\n\n")

for x in myresult:
	print(x)

print("\n\n")

for x in myresult:
	print(x[0], x[1], x[2])

# Closing the connection
cursor.close()
conexionBBDD.close()

input("Press ENTER to EXIT")