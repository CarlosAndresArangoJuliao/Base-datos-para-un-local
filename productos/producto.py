
import usuarios.conexion as conexion

connect = conexion.conectar()    # variable connect llamar metodo conectar que esta dentro de coexion
database = connect[0]            #indice cero donde eeta la base de datos
cursor = connect[1]              #indice uno  donde esta el cursor


class Producto:

    def __init__(self,codigo_producto,id_TipoPro, nombreProducto,familia,DNI_provedor,descripcion,cantidad_stock,precio_venta,precio_provedor):
        self.codigo_producto = codigo_producto
        self.id_TipoPro  = id_TipoPro
        self.nombreProducto = nombreProducto
        self.familia = familia
        self.DNI_provedor = DNI_provedor
        self.descripcion = descripcion
        self.cantidad_stock = cantidad_stock
        self.precio_venta = precio_venta
        self.precio_provedor = precio_provedor

    

    def guardar (self):
        sql = "INSER INTO productos VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
        producto =(self.codigo_producto,self.id_TipoPro,self.nombreProducto,self.familia,self.DNI_provedor,self.descripcion,self.cantidad_stock,self.precio_venta,self.precio_provedor)

        cursor.execute(sql,producto)
        database.commit()

        return[cursor.rowcount,self]

            #consulta producto existe
    def identificar_producto (self): #metodo identificar
        sql = "SELECT * FROM tipoproducto WHERE id_TipoPro = %s OR nombreProducto = %s"

         #DATOS PARA CONSULTA PRODUCTO
        producto = (self.id_TipoPro, self.nombreProducto)

        #CONSULTA
        cursor.execute(sql, producto)
        result = cursor.fetchone()

        return result
