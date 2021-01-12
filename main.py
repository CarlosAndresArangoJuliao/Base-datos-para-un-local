"""

Proyecto python  y Mysql  para un vivero deplantas
-Abrir el asistente
-Login y registro manejo base de datos
-registro, creara un nuevo usuario y asignara permisos
-permisos: crear nuevo producto, modificar producto, borrar producto, ingresar una venta,mostrar inventario
-login, identificara usuario y preguntara que quiere hacer segun los permisos
-opcion 1: crear nuevo producto, modificar producto, borrar producto, ingresar una venta,mostrar inventario
-opcion 2: ingresar venta, ver inventario

"""

from usuarios import acciones     #Importamos el MODULO acciones desde el PAQUETE de usuarios
print("""
Acciones disponibles:
    -Registro
    -Login

""")

haga = acciones.Acciones() #creamos una varibles 'haga' llamanos el modulo.Acciones o instanciamos la clase
acciones_ini=input("Bienvenido, quieres logearte o crear un nuevo registro:")
acciones_iniciales = acciones_ini.lower() #Con este comando solucionamos que el usuario ingrese en mayuculas o minusculas

if acciones_iniciales == "registro":
    haga.registro() #invoca el objeto registro

elif acciones_iniciales == "login":
    haga.login() #invoca el objeto login

