
DROP DATABASE IF EXISTS Proyecto_BBDD;
CREATE DATABASE Proyecto_BBDD;
use Proyecto_BBDD;


CREATE TABLE TipoProducto(
    id_TipoProd             int auto_increment not null PRIMARY key,
    nombreTipo              varchar (45) not null
);

CREATE TABLE producto (
    cod_producto            VARCHAR(15) NOT NULL PRIMARY KEY,
    Familia					VARCHAR(30) NOT NULL,
    descripcion 			text NULL,
    cantidad_stock 		    int NOT NULL,
    precio_venta 			NUMERIC(15,2) NOT NULL,
    precio_compra 		    NUMERIC(15,2) DEFAULT NULL,
    id_TipoPro           	INT,
    DNI_provedor            int (20),
    FOREIGN KEY (id_TipoPro) REFERENCES TipoProducto(id_TipoPro)
 );

CREATE TABLE TipoUsuario(
    id_TipoUsu              INT auto_increment not null PRIMARY key,
    cargo                   varchar(20),
    permisoTotal            varchar(2),
    permisoParcial          varchar(2)
    
);

CREATE TABLE usuarios(

    id_Usuario              int (25) auto_increment not null,
    nombre                  varchar (50),
    apellidos               varchar (50),
    Telefono                varchar(50),
    email                   varchar(255) not null,
    password                varchar (50) not null,
    fecha                   date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT uq_email UNIQUE(email)  
)ENGINE=InnoDb;

CREATE TABLE provedor (
    DNI_provedor            int(25) not null PRIMARY KEY,
    nombre                  varchar(40),
    direccion               varchar(255),
    telefono                varchar(50),
    email                   varchar(255)

);

CREATE TABLE pedido (
    
    cod_pedido 		        VARCHAR(25) NOT NULL,
    DNI_provedor			VARCHAR(50) DEFAULT NULL,
    fecha_pedido 			date NOT NULL,
    fecha_esperada 		    date NOT NULL,
    fecha_entrega 		    date DEFAULT NULL,
    estado 				    VARCHAR(15) NOT NULL,
    precio_compra 		    NUMERIC(15,2) NOT NULL,
    descripcion_pedido      VARCHAR(255) NOT NULL,
    PRIMARY KEY (cod_pedido),
    FOREIGN KEY (DNI_provedor) REFERENCES provedor(DNI_provedor)
);

CREATE TABLE detallePedido (

    cod_pedido              VARCHAR(25),
    id_Tipo_Producto        INT,
    cantidad                int,
    FOREIGN KEY (cod_pedido) REFERENCES pedido(cod_pedido),
    FOREIGN KEY (id_Tipo_Producto) REFERENCES TipoProducto(id_Tipo_Producto)

);

CREATE TABLE detalleVenta (
    
    cod_venta    		    VARCHAR (40) NOT NULL,
    cod_producto            VARCHAR(15),
    cantidad                int,
    cantidad_stock          int,
    CONSTRAINT pk_venta PRIMARY KEY (cod_venta)
        
);

CREATE TABLE venta (
    
    cod_venta    		    VARCHAR (40) NOT NULL,
    fecha_venta             VARCHAR(15),
    id_ususario 		    TEXT,
    DNI_cliente             INTEGER,
    forma_pago 			    VARCHAR (40) NOT NULL,
    fecha_pago 			    date NOT NULL,
    valor_total 			INTEGER(15) NOT NULL,
    CONSTRAINT pk_venta PRIMARY KEY (cod_venta)

);      

CREATE TABLE Cambio (
    
    cod_venta    		    VARCHAR (40) not null,
    id_TipoProd             int,
    fecha_venta			    date NOT NULL,
    fecha_cambio 			date NOT NULL,
    cantidad                int,
    cantidad_stock          int,
    DNI_cliente             INTEGER,
    observacion 			varchar (255),
    valor_total 		    INTEGER(15),
    CONSTRAINT pk_cambio PRIMARY KEY (cod_venta),
    FOREIGN KEY (id_TipoProd ) REFERENCES TipoProducto(id_TipoProd)
);

CREATE TABLE cliente (
    DNI_cliente             INTEGER not NULL PRIMARY KEY,
    nombre                  varchar (50),
    telefono                varchar(50),
    email                   varchar(255),
    direccion               varchar(255)

);