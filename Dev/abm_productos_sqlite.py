# Importamos los módulos necesarios para el proyecto
import sqlite3
from colorama import init, Fore

# Inicializamos colorama para mejorar la interfaz en la terminal
init(autoreset=True)


# Conexion a la base de datos
conexion = sqlite3.connect("inventario.db")

# Crear la tabla y carga de algunos registros
cursor = conexion.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    cantidad INTEGER NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT)
               """)
conexion.commit()

def validar_nonullo(nombre):
    ''' Funcion de validacion de campo vacio '''
    while True:
        campo = input(f"Ingrese {nombre} del producto: ")
        if campo != '':
            return campo
        print(Fore.RED + f"[WARNING] El {nombre} no puede estar vacio")

def validar_precio():
    ''' Funcion de validacion del precio '''
    while True:
        try:
            precio = float(input("Ingrese el Precio del producto: "))
            if precio > 0:
                return precio
            print(Fore.RED + "El precio debe ser mayor a 0.")
        except ValueError:
            print(Fore.RED + "[WARNING] Entrada no válida. Debe ingresar un número decimal mayor a 0.")

def validar_cantidad():
    ''' Funcion de validacion de la cantidad'''
    while True:
        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad >= 0:
                return cantidad
            print(Fore.RED + "El stock no puede ser negativo.")
        except ValueError:
            print(Fore.RED + "[WARNING] Entrada no válida. Debe ingresar un número entero.")


def registrar_producto():
    """Función para registrar un producto"""
    nombre = validar_nonullo('Nombre')
    descripcion = input("Ingrese la descripcion del producto: ").strip()
    precio = validar_precio()
    cantidad = validar_cantidad()
    categoria = input("Categoria: ")

    cursor.execute(f"""INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                     VALUES ('{nombre}', '{descripcion}', {cantidad}, {precio}, '{categoria}')""")
    conexion.commit()

def consultar_producto():
    """Función para consultar un producto"""
    # Validacion del ID producto
    while True:
        try:
            id = int(input("Ingrese el ID del producto: "))
            if id >= 0:
                break
            print("El id no puede ser negativo.")
        except ValueError:
            print(Fore.RED + "[WARNING] Entrada no válida. Debe ingresar un número entero.")
    
    # Consulta a la BD
    producto = cursor.execute(f"SELECT * FROM productos WHERE id={id}").fetchall()
    if producto:
        print("-" * 90)
        print("{:6}| {:10}| {:30}| {:8} | {:8} | {:10}".format("Código","Nombre","Descripcion","Cantidad","Precio","Categoria"))
        print("-" * 90)
        print("{:6}| {:10}| {:30}| {:8} | {:8} | {:10}".format(*producto[0]))
        print("-" * 90)
    else: 
        print(Fore.RED + "[WARNING] El producto no existe, volve a intentarlo.")


def actualizar_producto():
    """Función para actualizar un producto"""
    codigo = input("Ingrese el código del producto a actualizar: ")
    producto = cursor.execute(f"SELECT 1 FROM productos WHERE id='{codigo}'").fetchall()
    if producto:
        print("Ingrese los nuevos datos del producto:")
        nombre = validar_nonullo('Nombre')
        descripcion = input("Descripcion: ")
        cantidad = validar_cantidad()
        precio = validar_precio()
        categoria = input("Categoria: ")
        cursor.execute(f"""UPDATE productos SET nombre='{nombre}', descripcion='{descripcion}', cantidad={cantidad},
                                 precio={precio}, categoria='{categoria}'
                           WHERE id = '{codigo}'
                        """)
    
        print(Fore.GREEN + f"Producto '{nombre}' actualizado con éxito.")
    else: 
        print(Fore.RED + "[WARNING] El producto no existe, volve a intentarlo.")


def eliminar_producto():
    """Función para eliminar un producto"""
    # Validacion del ID producto
    while True:
        try:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            if id >= 0:
                break
            print("El id no puede ser negativo.")
        except ValueError:
            print(Fore.RED + "[WARNING] Entrada no válida. Debe ingresar un número entero.")

    productos = cursor.execute(f"SELECT 1 FROM productos WHERE id={id}").fetchall()
    if productos:
        cursor.execute(f"DELETE FROM productos WHERE id={id}")
        print(Fore.GREEN + f"Producto eliminado con éxito.")
    else: 
        print(Fore.RED + "[WARNING] El producto no existe, volve a intentarlo.")
        
        

def listar_productos():
    """Función para listar todos los productos"""
    productos = cursor.execute(f"SELECT * FROM productos").fetchall()
    if productos:
        print("\nLista completa de productos:")
        print("-" * 90)
        print("{:6}| {:10}| {:30}| {:8} | {:8} | {:10}".format("Código","Nombre","Descripcion","Cantidad","Precio","Categoria"))
        print("-" * 90)
        for row in productos: 
            print("{:6}| {:10}| {:30}| {:8} | {:8} | {:10}".format(*row))
        print("-" * 90)
    else:
        print("No hay productos registrados.")

        

def reporte_bajo_stock():
    """Función para mostrar productis con bajo stock"""
    while True:
        try:
            limite = int(input("Ingrese el límite de stock para el reporte: "))
            if limite >= 0:
                break
            print(Fore.RED + "El límite de stock no puede ser negativo. Inténtelo de nuevo.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Debe ser un número entero.")

    productos_bajo_stock = cursor.execute(f"SELECT id,nombre,cantidad FROM productos WHERE cantidad < {limite}").fetchall()
    if productos_bajo_stock:
        print("\nProductos con bajo stock: ")

        print(Fore.YELLOW + "+----+----------------------+----------+")
        print(Fore.YELLOW + "| ID | Nombre               | Cantidad |")
        print(Fore.YELLOW + "+----+----------------------+----------+")

        for row in productos_bajo_stock:
            print(Fore.YELLOW + "|{:3} |{:21} |{:9} |".format(*row))
        print(Fore.YELLOW + "+----+----------------------+----------+")
    else:
        print(Fore.GREEN + "No hay productos con bajo stock.")





#Menú interactivo
def menu():
    """Menú principal de la aplicación"""
    while True:
        print()
        print(Fore.CYAN +"-"*40)
        print(Fore.CYAN + "Menú Principal")
        print(Fore.CYAN +"-"*40)
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            listar_productos()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.CYAN + "Saliendo de la aplicación...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.\n")

#------------------------------------------------------------------------------
# Programa principal.
#------------------------------------------------------------------------------
menu()       # Iniciamos la aplicación mostrando el menú
conexion.close() # Cerramos la conexión a la base de datos al finalizar