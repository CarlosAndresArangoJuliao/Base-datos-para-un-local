
import mysql.connector 

def conectar():
    #colocamos los datos para conectarnos a la base de edatos
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "proyecto_bbdd",
        port = "3306"  #puerto donde trabaja myAdminsql

    )
    #print(database) #probamops si tenemos conecion con la base de datos
    cursor = database.cursor (buffered= True)  #Creamos cursos para poder llegar base de datos y le damos BUFFERED =TRUE para poder utilizar el mismo cursor en varias consultas

    return [database,cursor]
