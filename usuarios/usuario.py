import datetime
import hashlib
import usuarios.conexion as conexion



connect = conexion.conectar()    # variable connect llamar metodo conectar que esta dentro de coexion
database = connect[0]            #indice cero donde eeta la base de datos
cursor = connect[1]              #indice uno  donde esta el cursor


class Usuario:

    def __init__ (self, nombre, apellidos, email, password): #cosntructor  valores iniciales que llegan por parametro
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self): #se crea el metodo registro que nos devolvera el usuario registrado
        
        fecha = datetime.datetime.now()
        
                                #CIFRAR CONTRASEÑA

        cifrado = hashlib.sha256()    # metodo de cifrado metodo sha256()
        cifrado.update(self.password.encode('utf8')) #se utiliza el metodo de cifrado .encode('utf8')  pasa bites con metodo ENCODE
         

        sql = "INSERT INTO usuarios VALUES (null, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        #se crea el try y except, ya que esta parte es sencible a errores
                                  
        try:
            cursor.execute (sql,usuario)
            database.commit()
            result= [cursor.rowcount, self ]
        except:
            result= [0,self]

        return result


    def identificar (self): #metodo identificar
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()    # metodo de cifrado sha256()
        cifrado.update(self.password.encode('utf8')) #se utiliza el metodo de cifrado .encode('utf8')
        
        #DATOS PARA CONSULTA
        usuario = (self.email, cifrado.hexdigest())

        #CONSULTA
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result

    