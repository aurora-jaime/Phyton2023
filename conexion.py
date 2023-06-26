import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3308",
        database="mini_siau"
    )

    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES")

    for i in cursor:
        print(i)
    # print("Conexión correcta loba")

except mysql.connector.Error as e:
    print("Ocurrió un error:", e)

finally:
    conexion.close()
