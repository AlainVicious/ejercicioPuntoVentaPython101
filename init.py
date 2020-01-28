

# # import math
# # print(math.factorial(random.randint(5,10)))
# # print(math.fabs(-89))
# # print(math.exp(8))
# # print(math.pow(7,4))


# # import random
# # print(random.randint(10, 20))
# # print(random.randrange(10, 20, 5))
# # print(random.uniform(1,2))
# # print(random.choice(["ob1","ob2","ob3"]))


# # from datetime import datetime

# # hoy = datetime.now()

# # miFecha = datetime(1993,4,17)

# # print("año: ", miFecha.year)
# # print("mes: ", miFecha.month)
# # print("dia: ", miFecha.day)

# # miFecha = miFecha.replace(day=8)

# # print(miFecha)

# # import io


# # cadenaIO = io.StringIO("Cadena inicial")

# # cadenaIO.write(" segunda parte")


# # print(cadenaIO.getvalue())

# # cadenaIO.close()


# import os, stat

# # 4 = lectura
# # 2 = escritura
# # 1 = ejecucion
# # archivo1 = open('file1', 'x')
# # archivo1.write('file1')
# # print(os.access('file1', 7))
# # archivo1.close()

# # print(os.getcwd())

# # print(os.chdir('directorio1'))

# # print(os.getcwd())

# # archivo2 = open('file2', 'x')
# # archivo2.write('file2')
# # print(os.access('file2', 7))
# # archivo2.close()

# # print(os.access('archivo', stat.S_IRWXU))
# # os.chmod('archivo',stat.S_IRWXU)
# # print(os.access('archivo', 7))

# # # os.mkdir('newFolder')

# # os.remove('archivo')

# # os.rmdir('newFolder')


# # os.system('dir')


# # print(os.path.isfile('directorio1'))


# import sys

# print(sys.platform)
# print(sys.version)

# print(sys.getdefaultencoding())
# # sys.exit()




id_contacto apellido_paterno    apellido_materno    nombre_s    telefono    direccion
str         str                 str                 str         str         str

d01_directorio.csv
d01-01,Camacho,Luna,Fernando Alain,55-70-76-18-88,por alla
d01-02,Camacho,Luna,Fernando Alain,55-70-76-18-88,por alla
d01-03,Camacho,Luna,Fernando Alain,55-70-76-18-88,por alla
d01-04,Camacho,Luna,Fernando Alain,55-70-76-18-88,por alla
d01-05,Camacho,Luna,Fernando Alain,55-70-76-18-88,por alla

cada archivo de directorio debe quedar
de solo lectura

1.-Crear contacto
2.-Buscar contacto
3.-Eliminar Contacto
4.-Crear directorio
5.-Editar Contacto

1.-Crear Contacto
    lista de directorios disponibles
    (si no se creo uno antes se creara directorio.csv)

valida si existe un directorio
os.path.exists()








Punto de venta

bases de datos en archivos JSON

accesos.JSON

usuario_id:str
hash:str
intentos:int
status:int(1 activo 0 bloqueado)

usuarios.json
usuario_id:str
usr_name:str
rol:str(sys_admin,vendedor,supervisor)

productos.json
producto_id:str
producto:str
precio:float
descripcion:str
unidad_med:str(kg,litros,pieza,servicio)

inventario.json
producto_id:str
existencia:float

ventas.json
venta_id:int
usuario_id:str
total:float
articulos:[
    {
        producto_id:str,
        cantidad:float,
        pricio_unitario:float
    },
    {
        producto_id:str,
        cantidad:float,
        pricio_unitario:float
    }
]
roles:
sys_admin: dar de alta usuarios, cambiar contraseñas
vendedor:solo acceso a punto de venta
supervisor: punto de venta e inventario

programa:

pantalla 1

inicio de sesion
pedir usuario y contraseña
si falla a los 3 intentos bloquear usuario

pantalla 2
dependiendo el rol
rol sys_admin:
1)crear usuario
2)modificar usuario
    1)recuperar contraseña
    2)cambiar info

vendedor:

1)iniciar venta
    va recibiendo codigos del producto
    y regresando el producto o la lista de productos
    HASTA RECIBNIR EL COMANDO S
    ejemplo:

    in:
    leer producto: 1234567

    out:
    ID      PRODUCTO    CANT $UNI   TOTAL
    1234567 atun 250gr   1     2      2
    TOTAL                1            2

    IN:
    leer producto: 456123

    out:
    ID      PRODUCTO    CANT $UNI   TOTAL
    1234567 atun 250gr   1     2      2
    456123  botella agua 2     5      10
    TOTAL                3            12


cuando ce cierre la venta hacer los descuentos al inventario
e imprimir un ticket en un txt

supervisor
1) ventas(lo mismo que vendedor)
2) inventario


inventario
1)registrar entradas de producto
ingresar id de productosi este ya existe
imprimira su informacion
y dara las sig opciones

salida:
ID      producto    descripcion     existencia
1234567 atun 250g   lata de atun... 5
1)editar informacion
    (edita los datos del producto)
2)entrada de almacen
    (registra entrada o salida del producto al almacen)

si no existe el codigo
imprime:
el producto (id) no existe desea crearlo?