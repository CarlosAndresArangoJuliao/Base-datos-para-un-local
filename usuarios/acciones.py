
#Importamos el MODELO usuario del  PAQUETE usuarioS  NOTA pongo un ALIAS  para simplificar
import usuarios.usuario as modelo
import productos.acciones

class Acciones: 

    def registro (self):
        print (" \n Ok!! Vamos a registrarte en el sistema...")

        nombre= input("\n Cual es tu nombre?  ")
        apellidos= input("\n Cuales son tus apellidos?  ")
        email= input("\n Introduce tu email: ")
        password= input(" \n introduce tu passwword o contraseña:  ")
    #Variable usuario creamos el objeto en base a la clase del modulo Usuario, pasan las  propiedades, nombre, apellido..
        usuario = modelo.Usuario(nombre, apellidos, email,password) #llama del  class Usuario

    # registramos a usuario  en la basse de datos con una nueva variable registro
        registro = usuario.registrar()

    #comprobacion

        if registro [0] >=1:# define si se registro el usuario
            print (f"Perfecto{registro[1].nombre} Te has registrado correctamente con el email {registro[1].email}")

        else:
            print("No te has registrado correctemente")

           # ///////////////////////////////////////////////////////
    
    def login(self):  #creamos el objeto login

        print ("\n Bienbenido, identificate en el sistema.")

        try:
            email = input ("Introduce tu email: ")
            password = input("ingresa tu contraseña de registro: ")

            usuario = modelo.Usuario( '', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\n Bienvenido {login[1]},te has logiado correctamente y te registraste el: {login[5]}")
                self.proximasAcciones(login)
            
               

        except Exception as e:
            print("\n ")
            print (type (e))
            print (type (e).__name__)  #poder sacar el error emn concreto
            print (f"Login incorrecto!!! Intentalo de nuevo.")


            #///////////////////////////////////////////////////////////////

    def proximasAcciones (self, usuario):
        print("""

        Acciones siguientes:

        -Ver inventario (inventario)
        -Registrar  venta nueva (venta)
        -Ingresar un producto (ingresar) 
        -Modificar un producto (modificar)
        -Borrar un producto (borrar)
        -pedidos realizados(pedido)
        -devolucion de vemtas (devolucion)
        -Salir (salir)
        """)
        accion = input ("\n¿Que Quieres hacer?: ")
        accion1 = accion.lower()

        hazEl = productos.acciones.Acciones()

        if accion1 == "inventario":
            print (f"el inventarios al dia de hoy {usuario[5]} es: ")
            self.proximasAcciones(usuario)

        elif accion1 == "venta":
            print("el pago realizado es: ")
            self.proximasAcciones(usuario)

        elif accion1 == "ingresar":
            hazEl.ingresar(usuario)
            self.proximasAcciones(usuario)

        elif accion1 == "modificar":
            print("Que producto quieres modificar: ")
            self.proximasAcciones(usuario)

        elif accion1 == "borrar":
            print("Que producto quieres quitar: ")
            self.proximasAcciones(usuario)

        elif accion1 == "devolucion":
            print("igresa codigo de la factura de venta: ")
            self.proximasAcciones(usuario)


        elif accion1 == "pedido":
            print("Ingrese codigo del pedido: ")
            self.proximasAcciones(usuario)

        if accion1 == "salir":
            print(f"Muchas gracias, hata luego {usuario[1]}!!!")
            exit()
        else:
            print("\n Ingresaste mal la opcion!!!!, vuelve a intenatrlo :) ")
            self.proximasAcciones(usuario)

        
    