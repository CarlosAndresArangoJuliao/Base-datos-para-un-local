import productos.producto  as modelo

class Acciones:


    
    def ingresar (self,usuario):
        print (f"\n {usuario[1]},Vamos a ingresar un producto. ")

        id = input ("introduce el id del producto: ")
        nombre = input ("introduce nombre del producto")

        if  id == ingresar [0]:
            print("\n Este producto ya esta en el inventario ! ")
            cantidad_prod = input ("\n ingrese la cantidad a sumar en la existencia: ")  
            cantidad_stock += cantidad_prod; 
            print(f"Agregaste {cantidad_prod}, quedando un total en stock de : {cantidad_stock}; el dia {ingresar[5]} ")

            